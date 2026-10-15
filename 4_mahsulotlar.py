import csv

jami = 0

with open("products_homework.csv", encoding="utf-8-sig", newline="") as fayl:
    qatorlar = csv.DictReader(fayl)

    for qator in qatorlar:
        narx = float(qator["price"])
        miqdor = int(qator["quantity"])
        qiymat = narx * miqdor
        print(qator["name"], "-", qiymat)
        jami += qiymat

print("Umumiy qiymat:", jami)
