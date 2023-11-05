import random


def random_number(x):
    y = random.randint(1, 7)
    print(y)
    if x == y:
        return True
    else:
        return False


print(random_number(5))
