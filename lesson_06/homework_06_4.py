#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers_list = [1, 5, 6, 89, 41, 3, 42, 2, 4]
sum_of_even_numbers = sum(num for num in numbers_list if num % 2 == 0)
print(f"Сума парних чисел становить: {sum_of_even_numbers}")