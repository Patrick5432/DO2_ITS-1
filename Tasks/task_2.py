import math

weith = float(input("Введите вес пациента: "))
days = int(input("Введите количество дней в курсе лечения: "))

numberPillsOnWeith = (weith * 10) / 250
numberPillsOnWeith = round(numberPillsOnWeith, 1)

print(f"Нужно принимать по {numberPillsOnWeith} таблетки(-e) 2 раза в день")
print(f"Необходимо {math.ceil(((numberPillsOnWeith * days) * 2) / 50)} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения")