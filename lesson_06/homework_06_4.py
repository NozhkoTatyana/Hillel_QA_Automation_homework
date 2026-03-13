#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers_list = [1,5,6,89,41,3,42,2,4]
sum_of_even_numbers = 0

for number in numbers_list:
    if number % 2 == 0:
        sum_of_even_numbers += number
print(f'Сума парних чисел становить: {sum_of_even_numbers}')

