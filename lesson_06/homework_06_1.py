# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()


text = input("Введіть рядок: ")
unique_once = []

for ch in text:
    if text.count(ch) == 1:
        unique_once.append(ch)

if len(unique_once) > 10:
    print("True", unique_once)
else:
    print("False", unique_once)
