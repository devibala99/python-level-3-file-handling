import os
from analyzer import analyze_logs

BASE_DIR = os.path.dirname(__file__)
LOG_FILE = os.path.join(BASE_DIR, "sample.log")
REPORT_FILE = os.path.join(BASE_DIR, "report.txt")

def write_report(summary):
    with open(REPORT_FILE, "w") as file:
        file.write("LOG ANALYSIS REPORT\n")
        file.write("-------------------\n")
        file.write(f"Total Lines: {summary['total']}\n")
        file.write(f"INFO: {summary['INFO']}\n")
        file.write(f"WARNING: {summary['WARNING']}\n")
        file.write(f"ERROR: {summary['ERROR']}\n\n")

        file.write("ERROR DETAILS:\n")
        for error in summary["errors"]:
            file.write(error + "\n")

def main():
    summary = analyze_logs(LOG_FILE)

    print("Log Analysis Completed")
    print(f"Total Lines: {summary['total']}")
    print(f"INFO: {summary['INFO']}")
    print(f"WARNING: {summary['WARNING']}")
    print(f"ERROR: {summary['ERROR']}")

    write_report(summary)
    print("Report saved to report.txt")

if __name__ == "__main__":
    main()
