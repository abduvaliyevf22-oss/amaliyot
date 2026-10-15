import csv

jami = 0
son = 0

with open("orders_homework.csv", encoding="utf-8-sig", newline="") as fayl:
    qatorlar = csv.DictReader(fayl)

    for qator in qatorlar:
        jami += float(qator["amount"])
        son += 1

if son > 0:
    print("Buyurtmalar yig'indisi:", jami)
    print("O'rtacha buyurtma qiymati:", jami / son)
