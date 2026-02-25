# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(banana)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = 1 + 2 + 3 + 4
print(perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
def trees():
    all_trees = 0
    apple_tr = 4
    pear_tr = apple_tr + 5
    plum_tr = apple_tr - 2
    all_trees = apple_tr + pear_tr + plum_tr
    return all_trees

print(trees())

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
def evening_temperature():
    temp = 5
    temp -= 10
    temp += 4
    return temp

print(evening_temperature())

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
def theatre_group():
    boys = 24
    girls = int(boys / 2)
    boys_today = boys - 1
    girls_today = girls - 2
    total_today = boys_today + girls_today
    return total_today

print(theatre_group())

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
def books_cost():
    first_b = 8
    second_b = first_b + 2
    third_b = (first_b + second_b) / 2
    total = first_b + second_b + third_b
    return total

print(books_cost())
