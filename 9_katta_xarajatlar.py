import csv

with open("expenses_homework.csv", encoding="utf-8-sig", newline="") as fayl:
    qatorlar = csv.DictReader(fayl)

    with open("large_expenses.csv", "w", encoding="utf-8-sig", newline="") as yangi_fayl:
        yozuvchi = csv.DictWriter(yangi_fayl, fieldnames=["category", "amount"])
        yozuvchi.writeheader()

        for qator in qatorlar:
            if float(qator["amount"]) > 200:
                yozuvchi.writerow({
                    "category": qator["category"],
                    "amount": qator["amount"]
                })

print("Katta xarajatlar large_expenses.csv fayliga yozildi")
