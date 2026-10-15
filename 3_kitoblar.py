import csv

son = 0

with open("books_homework.csv", encoding="utf-8-sig", newline="") as fayl:
    qatorlar = csv.DictReader(fayl)

    for qator in qatorlar:
        if int(qator["year"]) > 2021:
            son += 1

print("2021-yildan keyin nashr etilgan kitoblar:", son)
