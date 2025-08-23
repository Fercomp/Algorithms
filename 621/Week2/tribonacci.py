# Tabulation approach
def tribonacci(n):
    tab = [0] * (n + 1)
    tab[0] = 0
    if n >= 1:
        tab[1] = 1
    if n >= 2:
        tab[2] = 2
        
    if n >= 3:
        for i in range(3, n+1):
            tab[i] = tab[i-1] + tab[i-2] + tab[i-3]
    
    return tab[n]


while True:
    n = int(input())
    if n == 0:
        break
    print(tribonacci(n) %  1000000009)