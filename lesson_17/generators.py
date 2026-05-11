def even_numbers(n):
    """
    генератор, який повертає послідовність парних чисел від 0 до N
    """
    for i in range(0, n+1, 2):
        yield i

def fibonacci(n):
    """
    генератор, який генерує послідовність Фібоначчі до певного числа N
    """
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b



if __name__ == '__main__':
    print(list(even_numbers(9)))
    print(list(fibonacci(20)))


