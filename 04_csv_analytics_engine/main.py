import os
from analytics import analyze_sales

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "sales.csv")
REPORT_FILE = os.path.join(BASE_DIR, "report.txt")

def write_report(result):
    with open(REPORT_FILE, "w") as file:
        file.write("SALES ANALYTICS REPORT\n")
        file.write("----------------------\n\n")

        file.write(f"Total Revenue: {result['total_revenue']}\n\n")

        file.write("Revenue by Category:\n")
        for category, amount in result["category_revenue"].items():
            file.write(f"- {category}: {amount}\n")

        file.write("\nRevenue by Region:\n")
        for region, amount in result["region_revenue"].items():
            file.write(f"- {region}: {amount}\n")

def main():
    result = analyze_sales(DATA_FILE)

    print("CSV Analysis Completed")
    print("Total Revenue:", result["total_revenue"])

    write_report(result)
    print("Report saved to report.txt")

if __name__ == "__main__":
    main()
