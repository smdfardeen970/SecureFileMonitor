
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Project directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MONITOR_DIR = os.path.join(BASE_DIR, "monitored_files")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Create directories if missing
os.makedirs(MONITOR_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "file_monitor.log"),
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

class MonitorHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            message = f"FILE CREATED: {event.src_path}"
            print(message)
            logging.info(message)

    def on_modified(self, event):
        if not event.is_directory:
            message = f"FILE MODIFIED: {event.src_path}"
            print(message)
            logging.info(message)

    def on_deleted(self, event):
        if not event.is_directory:
            message = f"FILE DELETED: {event.src_path}"
            print(message)
            logging.info(message)
    def on_moved(self, event):
        if not event.is_directory:
            message = f"FILE MOVED: {event.src_path} -> {event.dest_path}"
            print(message)
            logging.info(message)
if __name__ == "__main__":
    observer = Observer()
    handler = MonitorHandler()

    observer.schedule(handler, MONITOR_DIR, recursive=True)
    observer.start()

    print("SecureFileMonitor started!")
    print(f"Monitoring: {MONITOR_DIR}")
    print("Press CTRL+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
