from datetime import datetime

def send_alert(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    alert = f"[{time}] SECURITY ALERT: {message}"

    print("\033[91m" + alert + "\033[0m")

    with open("security_alerts.log", "a") as f:
        f.write(alert + "\n")

send_alert("Unauthorized file modification detected!")

