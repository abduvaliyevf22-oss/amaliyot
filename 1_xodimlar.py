import csv

with open("employees_homework.csv", encoding="utf-8-sig", newline="") as fayl:
    qatorlar = csv.DictReader(fayl)

    for qator in qatorlar:
        print(qator["name"], "-", qator["department"])
