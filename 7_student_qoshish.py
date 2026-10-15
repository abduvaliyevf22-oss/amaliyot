import csv

ism = input("Student ismi: ")
yosh = int(input("Yoshi: "))
ball = int(input("Ball: "))

if ball >= 70:
    with open("new_students_homework.csv", "a", encoding="utf-8-sig", newline="") as fayl:
        yozuvchi = csv.writer(fayl)
        yozuvchi.writerow([ism, yosh, ball])

    print("Student faylga qo'shildi")
else:
    print("Ball 70 dan kam. Fayl o'zgartirilmadi.")
