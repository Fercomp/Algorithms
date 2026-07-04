import math

EPS = 1e-9

class Point2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    # --- Operadores ---
    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Point2D':
        return Point2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Point2D':
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> 'Point2D':
        if scalar == 0:
            raise ValueError("Não é possível dividir por zero.")
        return Point2D(self.x / scalar, self.y / scalar)
        
    # --- Operadores "in-place" (como +=, -=, etc.) ---

    def __iadd__(self, other: 'Point2D') -> 'Point2D':
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other: 'Point2D') -> 'Point2D':
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, scalar: float) -> 'Point2D':
        self.x *= scalar
        self.y *= scalar
        return self

    def __itruediv__(self, scalar: float) -> 'Point2D':
        if scalar == 0:
            raise ValueError("Não é possível dividir por zero.")
        self.x /= scalar
        self.y /= scalar
        return self

    # This is important so we can do sort in a list of points  
    def __lt__(self, other: 'Point2D') -> bool:
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y
    
    # This is importante to compare, uses EPS to avoid precision error 
    def __eq__(self, other: 'Point2D') -> bool:
        return (abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS)

if __name__ == '__main__':
    p1 = Point2D(1, 2)
    p2 = Point2D(3, 4)

    print(f"Ponto 1: {p1}")
    print(f"Ponto 2: {p2}")

    # Usando os operadores sobrecarregados
    soma = p1 + p2
    print(f"Soma (p1 + p2): {soma}")

    diferenca = p1 - p2
    print(f"Diferença (p1 - p2): {diferenca}")

    mult = p1 * 3
    print(f"Multiplicação (p1 * 3): {mult}")

    mult_refletida = 2.5 * p2
    print(f"Multiplicação refletida (2.5 * p2): {mult_refletida}")

    div = p2 / 2
    print(f"Divisão (p2 / 2): {div}")

    # Testando operadores in-place
    print("-" * 20)
    p_inplace = Point2D(10, 20)
    print(f"Ponto original para teste in-place: {p_inplace}")

    p_inplace += Point2D(1, 1)
    print(f"Depois de += Point2D(1, 1): {p_inplace}") # Deve ser (11, 21)

    p_inplace *= 2
    print(f"Depois de *= 2: {p_inplace}") # Deve ser (22, 42)