import csv

ballar = []

with open("exam_results_homework.csv", encoding="utf-8-sig", newline="") as fayl:
    qatorlar = csv.DictReader(fayl)

    for qator in qatorlar:
        ballar.append(int(qator["score"]))

if ballar:
    print("Eng yuqori ball:", max(ballar))
    print("Eng past ball:", min(ballar))
    print("O'rtacha ball:", sum(ballar) / len(ballar))
    print("70 yoki undan yuqori ball olganlar:", sum(1 for ball in ballar if ball >= 70))
