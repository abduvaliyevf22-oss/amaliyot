import csv

with open("inventory_homework.csv", encoding="utf-8-sig", newline="") as fayl:
    qatorlar = list(csv.DictReader(fayl))

eng_kam = min(qatorlar, key=lambda qator: int(qator["stock"]))
print("Eng kam qolgan mahsulot:", eng_kam["item"])
print("Soni:", eng_kam["stock"])
