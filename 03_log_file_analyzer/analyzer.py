
def analyze_logs(file_path):
    summary = {
        "total": 0,
        "INFO" : 0,
        "WARNING" : 0,
        "ERROR": 0,
        "errors": []
    }

    with open(file_path, "r") as file:
        for line in file:
            summary["total"] += 1

            if " INFO " in line:
                summary["INFO"] += 1
            elif " WARNING " in line:
                summary["WARNING"] += 1
            elif " ERROR " in line:
                summary["ERROR"] += 1
                summary["errors"].append(line.strip())

    return summary


            