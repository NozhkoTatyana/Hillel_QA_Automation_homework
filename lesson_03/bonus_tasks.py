def solution(x):
    first_digit = x // 100
    second_digit = (x // 10) % 10
    third_digit = x % 10
    value = third_digit * 100 + second_digit * 10 + first_digit
    return value

print(solution(100))
print(solution(257))
print(solution(888))