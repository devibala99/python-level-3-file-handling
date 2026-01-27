import csv

def analyze_sales(file_path):

    total_revenue = 0
    category_revenue = {}
    region_revenue = {}

    with open(file_path, newline ="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = int(row["amount"])
            category = row["category"]
            region = row["region"]

            total_revenue += amount

            category_revenue[category] = category_revenue.get(category, 0) + amount
            region_revenue[region] = region_revenue.get(region, 0) + amount

        return {
            "total_revenue" :  total_revenue,
            "category_revenue" : category_revenue,
            "region_revenue" : region_revenue
        }
    










