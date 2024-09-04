import math

dose = int(input("Введите среднюю суточную дозировку в мг/кг (10 или 15): "))
weith = float(input("Введите вес пациента: "))
days = int(input("Введите количество дней в курсе лечения: "))

if (dose == 10 or dose == 15):
    numberPillsOnWeith = (weith * dose) / 250
    numberPillsOnWeith = round(numberPillsOnWeith, 1)

    print(f"Нужно принимать по {numberPillsOnWeith} таблетки(-e) 2 раза в день")
    print(f"Необходимо {math.ceil(((numberPillsOnWeith * days) * 2) / 50)} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения")
else:
    print("Суточная дозировка не равна 10 или 15 мг/кг! Остальные дозировки пока не рассчитываются!")