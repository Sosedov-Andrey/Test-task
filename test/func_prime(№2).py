import math

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def func_prime(x: int, y: int) -> list:
    lst_prime = []
    for i in range(x, y + 1):
        if is_prime(i):
            lst_prime.append(i)
    return lst_prime




func_prime(3, 27)