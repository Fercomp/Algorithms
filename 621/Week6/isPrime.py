import math

def eh_primo(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    limite = int(math.sqrt(x)) + 1
    for i in range(3, limite, 2):
        if x % i == 0:
            return False
    return True