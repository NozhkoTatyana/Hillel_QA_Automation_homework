def reverse_iterator(lst):
    """
    ітератор для зворотного виведення елементів списку
    """
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]


class EvenIterator:
    """ ітератор, який повертає всі парні числа в діапазоні від 0 до N """
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                val = self.current
                self.current += 1
                return val
            self.current += 1
        raise StopIteration



if __name__ == '__main__':
    for x in EvenIterator(11):
        print(x)

    for x in reverse_iterator([11, 6, 8, 9, 5]):
        print(x)








