import csv

input_file = "sales.csv"
output_file = "report.csv"

with open(input_file, "r", newline="", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)

    fieldnames = reader.fieldnames + ["total"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        units = int(row["units"])
        unit_price = float(row["unit_price"])
        row["total"] = f"{units * unit_price:.2f}"

        writer.writerow(row)

print(f"Report successfully written to {output_file}")