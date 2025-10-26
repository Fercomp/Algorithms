class DynamicArray:
    def __init__(self):
        self.capacity = 10  # Número de slots no array subjacente
        self.size = 0       # Número de elementos atualmente armazenados
        self.elements = [None] * self.capacity
    
    # Time: O(1)
    def get(self, i):
        # Comparamos com 'size' (elementos reais) e não 'capacity' (espaço alocado)
        if i < 0 or i >= self.size:
            raise IndexError('Index out of bounds')
        return self.elements[i]
    
    # Time: O(1)
    def set(self, i, x):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of bounds')
        self.elements[i] = x
    
    # Time: O(1)
    def get_size(self):
        # Uma alternativa "Pythonica" seria implementar __len__(self).
        return self.size 

    # Time: Pior caso O(n) (quando redimensiona), Amortizado O(1)
    def append(self, x):
        if self.size == self.capacity:
            # Dobra a capacidade se o array estiver cheio
            self.resizing(self.capacity * 2)
        
        self.elements[self.size] = x
        self.size += 1

    # Time: O(n) (onde n = self.size)
    def resizing(self, new_capacity):
        new_array = [None] * new_capacity
        
        # Copia apenas os elementos existentes (até self.size)
        for i in range(self.size):
            new_array[i] = self.elements[i]
            
        self.elements = new_array
        self.capacity = new_capacity
    
    # Time: Pior caso O(n) (se encolher), Amortizado O(1)
    def pop_back(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
            
        self.size -= 1
        item = self.elements[self.size] # Salva o item para retornar
        self.elements[self.size] = None  # Limpa o slot (ajuda o Garbage Collector)
        
        # Encolhe o array se o uso for <= 25% da capacidade, mas não encolhe abaixo de 10
        if self.size <= 0.25 * self.capacity and self.capacity > 10:
            new_capacity = max(10, self.capacity // 2) # Garante que não fique menor que 10
            self.resizing(new_capacity)
        
        return item
    
    # Time: O(n)
    def pop(self, i):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        
        item = self.elements[i]
        
        # Desloca todos os elementos da direita para a esquerda
        for j in range(i, self.size - 1):
            self.elements[j] = self.elements[j + 1]
        
        # O último elemento agora é um duplicado, então usamos pop_back
        self.pop_back()
        return item
    
    # Time: O(n)
    def contains(self, x):
        for i in range(self.size):
            if self.elements[i] == x:
                return i
        return -1
    
    # Time: O(n)
    def insert(self, i, x):
        # Permitimos inserir em i == self.size (equivale a append)
        if i < 0 or i > self.size:
            raise IndexError("Index out of bounds")

        # Se estiver cheio, redimensiona primeiro
        if self.size == self.capacity:
            self.resizing(self.capacity * 2)

        # Desloca elementos para a direita antes de inserir
        # Começa do fim (self.size) e vai até 'i'
        for j in range(self.size, i, -1):
            self.elements[j] = self.elements[j - 1]

        # Agora o slot 'i' está livre
        self.elements[i] = x
        self.size += 1

    # Time: O(n)
    def remove(self, x):
        index = self.contains(x)
        
        # Se não encontrou, não faz nada
        if index == -1:
            return False
            
        self.pop(index)
        return True