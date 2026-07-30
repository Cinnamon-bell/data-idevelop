import csv
total = 0
top1 = ""
top1_price = 0
top2 = ""
top2_price = 0
top3 = ""
top3_price = 0

with open('sales.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        total += float(row['unit_price'])
        if float(row['unit_price']) > float(top1_price):
            top3 = top2
            top2 = top1
            top1 = row['order_id'] + ' ' + row['product']
            top3_price = float(top2_price)
            top2_price = float(top1_price)
            top1_price = float(row['unit_price'])
        elif float(row['unit_price']) > float(top2_price):
            top3 = top2
            top2 = row['order_id'] + ' ' + row['product']
            top2_price = float(row['unit_price'])
        elif float(row['unit_price']) > float(top3_price):
            top3 = row['order_id'] + ' ' + row['product']
            top3_price = float(row['unit_price'])

print("Total unit price:", total)
print("Top 1 unit price:", top1, "with price:", top1_price)
print("Top 2 unit price:", top2, "with price:", top2_price)
print("Top 3 unit price:", top3, "with price:", top3_price)