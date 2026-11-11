import os
from datetime import datetime

report = []

report.append("SECURE FILE MONITOR - AUDIT REPORT")
report.append("=" * 40)
report.append("Date: " + str(datetime.now()))
report.append("")

files = ["logs/file_monitor.log", "security_alerts.log"]

for filename in files:
    report.append("\nFILE: " + filename)
    report.append("-" * 40)

    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read()

        report.append(content if content else "No records found.")
    else:
        report.append("Log file not found.")

report.append("\nEND OF AUDIT REPORT")

with open("audit_report.txt", "w") as f:
    f.write("\n".join(report))

print("Audit report generated successfully!")
print("Saved as audit_report.txt")

