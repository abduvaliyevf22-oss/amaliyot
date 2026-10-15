import csv

with open("students_homework.csv", encoding="utf-8-sig", newline="") as fayl:
    qatorlar = csv.DictReader(fayl)

    for qator in qatorlar:
        if int(qator["score"]) >= 85:
            print(qator["name"], "-", qator["score"])
