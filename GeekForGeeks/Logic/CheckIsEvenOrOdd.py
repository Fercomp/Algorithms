# Usando operador % 'resto' 
def is_even(n):
    return n % 2 == 0

# Usar bitwise operator & para ver o último bit do número (super rápido)
def is_even2(n):
    return (n & 1) == 0