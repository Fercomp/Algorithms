'''
(n + m) mod r = n mod r + m mod r
Encontre o resto da divisõ de 1991 + 1992 por 7
'''
print(1991 % 7)
'''
O resto de 1991 por 7 é 3 logo 1992 é 4.
Com 1991 eu consegui agrupar grupos com 7 e sobrou 3
ja com 1992 eu agrupei em 7 e sobrei 4, no final juntando as duas sobras
ficamos com mais um grupo logo resto zero 
'''

'''
n * m mod r = (n mod r * m mod r) mod r
Encontre o resto da divisão de 1991 * 1992 por 7
1991 = 7q + 3
1992 = 7k + 4
1991 = (7q + 3).(7k + 4) = 49k^2 + 4.7q + 3.7.k + 12
Note que todos os elementos da soma é divisível por 7 basta saber
se o 12 é divisível por 7, seu resto é 5 logo o resto da multiplicação
é 5
'''

'''
n ^ k mod r = ((n mod r) ^ k) mod r
'''

'''Encontre o resto da divisão de 9^100 por 8
(8 + 1)(8 + 1)(8 + 1)... tem resto 1, unico valor não multiplicado por 8
'''

'''
Se dois numero tem resto r divididos por k a sua subtração sera divisivel por k'''

n = 92910
m = 1298
r = 17
(n + m) % r == ((n % r) + (m % r)) % r
# multi 
# expo
# Algoritmo de euclides