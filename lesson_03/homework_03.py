#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = """\
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
"""

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for word in alice_in_wonderland.split():
    if "'" in word:
        print(f"Знайдено одинарну лапку в слові: {word}")
print("=" * 40)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)
print("=" * 40)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_black_sea = 436402
area_azov_sea = 37800

task_04 = (f"The area of the Black Sea is {area_black_sea} km², and the area of the Azov Sea is {area_azov_sea} km².\n"
           f"What is the total area of the Black Sea and the Azov Sea together?")
print(task_04)
print("=" * 40)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
warehouses = 3
total_goods = 375291
goods_second_third = 222950
goods_first_second = 250449

task_05 = (f"A supermarket chain has {warehouses} warehouses, where a total of {total_goods} goods are stored. \n"
           f"In the first and second warehouses there are {goods_first_second} goods. \n"
           f"In the second and third warehouses there are {goods_second_third} goods. \n"
           f"Find the number of goods stored in each warehouse.")
print(task_05)
print("=" * 40)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
service_type = '"Installment Payment"'
monthly_payment = 1179
payment_period_months = 18    # 1.5 року = 18 місяців

task_06 = (f"Mykhailo and his parents decided to buy a computer using the {service_type} service. \n"
           f"It is known that they will have to pay for {payment_period_months} months \n"
           f"at {monthly_payment} UAH per month. Calculate the cost of the computer.")
print(task_06)
print("=" * 40)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
division_remainder = ['8019 : 8', '9907 : 9', '2789 : 5', '7248 :  6', '7128 : 5','19224 : 9']

task_07 = (f"Find the remainder when dividing the numbers:\n"
           f"a) {division_remainder[0]}           d) {division_remainder[3]}\n"
           f"b) {division_remainder[1]}           e) {division_remainder[4]}\n"
           f"c) {division_remainder[2]}           f) {division_remainder[5]}\n")
print(task_07)
print("=" * 40)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

order = {
    "Large pizza": {"quantity": 4, "price": 274},
    "Medium pizza": {"quantity": 2, "price": 218},
    "Juice": {"quantity": 4, "price": 35},
    "Cake": {"quantity": 1, "price": 350},
    "Water": {"quantity": 3, "price": 21}
}

items_str = "\n".join(
    f"{item:<20} {details['quantity']:<12} {details['price']} UAH"
    for item, details in order.items())

task_08 = (f"Iryna, preparing for her birthday, made a list of what she needs to order. Calculate how much money"
           f" will be needed for her order.\n"
           f"Item           Quantity           Price\n"
           f"{items_str}")
print(task_08)
print("=" * 40)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_per_page = 8
all_photos = 232

task_09 = (f"Ihor is engaged in photography. He decided to collect all his {all_photos} photographs and paste them\n"
           f"into an album. On one page, no more than {photos_per_page} photos can be placed. How many pages will\n"
           f"Ihor need to paste all the photos?")
print(task_09)
print("=" * 40)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_km = 1600
fuel_per_100km = 9
tank_capacity = 48

task_10 = (f"A family went on a car trip from Kharkiv to Budapest. "
           f"The distance between these cities is {distance_km} km. It is known that for every 100 km,\n"
           f"{fuel_per_100km} liters of gasoline are needed. The tank capacity is {tank_capacity} liters.\n"
           f"1) How many liters of gasoline will be needed for such a trip?\n"
           f"2) What is the minimum number of times the family will need to stop at a gas station "
           f"during this trip, refueling the full tank each time?")

print(task_10)
print("=" * 40)
