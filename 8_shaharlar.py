import csv

with open("cities_homework.csv", encoding="utf-8-sig", newline="") as fayl:
    qatorlar = csv.DictReader(fayl)

    for qator in qatorlar:
        if int(qator["population"]) > 500000:
            print(qator["city"])
