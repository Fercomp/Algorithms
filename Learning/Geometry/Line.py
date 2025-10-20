# na escola uma linha é dada por y = ax + b
# aqui vamos convensionar que são todos os pontos que estao na linha 
# ay + bx + c = 0, e b = 1 para linhas não verticais e b = 0 para verticais

class Line:
    def __init__(self, a=0, b,=0 c=0):
        self.a = a
        self.b = b
        self.c = c

# ay + bx + c = 0
# ay1 + bx1 + c = 0
# ay2 + bx2 + c = 0
# a(y1-y2) + b(x1-x2) = 0
# b(x1-x2) = -a(y1-y2)
# b = -a(y1-y2)/(x1-x2)
