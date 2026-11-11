
import hashlib
import json
import os

FOLDER = "monitored_files"
BASELINE = "baseline.json"

def get_hash(filepath):
    sha = hashlib.sha256()

    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)

    return sha.hexdigest()

current = {}

for filename in os.listdir(FOLDER):
    path = os.path.join(FOLDER, filename)

    if os.path.isfile(path):
        current[filename] = get_hash(path)

if not os.path.exists(BASELINE):
    with open(BASELINE, "w") as f:
        json.dump(current, f, indent=4)
    print("Baseline created successfully!")

else:
    with open(BASELINE, "r") as f:
        old = json.load(f)

    for filename, filehash in current.items():
        if filename not in old:
            print("NEW FILE:", filename)
        elif old[filename] != filehash:
            print("WARNING: FILE MODIFIED:", filename)

    for filename in old:
        if filename not in current:
            print("WARNING: FILE DELETED:", filename)

