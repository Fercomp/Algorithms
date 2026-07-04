# Achar pontos de transição em um array ordenado (Binary Search modificado) 
# Achar o primeiro commit que falha, ou o último que passa

commits = ["pass", "pass", "pass", "pass", "fail", "fail", "fail"]

def git_commit(commits):
    l = 0
    r = len(commits) - 1
    
    # Isso é enquanto a diferença de l e r é maior que 1, ou seja quando for 1 termina
    # Nesse caso teremos l e r consecutivos um do lado do outro
    while r > l + 1:
        mid = (l + r) // 2
        if commits[mid] == "pass":
            l = mid
        else:
            r = mid
            
    # l vai ser o último que passava e r vai ser o primeiro que falha
    return l, r

print(git_commit(commits)) # (3, 4)

# Dado um array de números positivos e um target value, encontre o maior número
# que elevado ao quadrado ainda é menor ou igual ao target se tiver.

squarables = [1, 3, 4, 5, 6, 7, 8, 11, 20, 21, 23, 25, 25]

def squared_target(nums, target):
    l = 0
    r = len(nums) -1
    
    # Caso o target seja menor que o menor dos números, ou o target seja maior que
    # o maior dos números então não tem o que procurar return -1
    if (nums[l] ** 2) > target or (nums[r] ** 2) < target:
        return -1
    
    while r > l + 1:
        mid = (l + r) // 2
        if nums[mid] ** 2 <= target:
            l = mid
        else:
            r = mid
            
    return nums[l]

print(squared_target(squarables, 36)) # 6

# Achar o primeiro elemento não negativo do array

integer = [-21, -15, -9, -5, -5, -1, -1, 0, 0, 4, 7, 12, 21]

def first_non_negative(nums):
    l = 0
    r = len(nums) -1
    while r > l + 1:
        mid = (l + r) // 2
        if nums[mid] < 0:
            l = mid
        else:
            r = mid
    return l

print(first_non_negative(integer)) # 6


# Achar a primeira palavra que começa com 'p'

words = ["apple", "banana", "peach", "strawberry"]

def first_with_p(words):
    l = 0
    r = len(words)
    
    while r > l + 1:
        mid = (l + r) // 2
        if words[mid][0] < "p":
            l = mid
        else:
            r = mid
            
    return words[r]

print(first_with_p(words)) # peach


# Em um array ordenado que permite duplicatas encontrar a última ocorrencia de um target
# se o target não está no array retornar o que está mais próximo

array = [1, 3, 5, 6, 7, 7, 8, 11, 13, 21]

def nearest_element(array, target):
    l = 0
    r = len(array) - 1
    
    while r > l + 1:
        mid = (l + r) // 2
        if array[mid] <= target:
            l = mid
        else:
            r = mid
            
    return l

print(nearest_element(array, 7)) # 5

# Voce recebe um deck com 52 cartas numeradas e ordenadas. Esse deck foi cortado 
# então em algum ponto a primeira metade foi colocado atrás da segunda metade 
# ambos em ordem [1, 2, 3, ... x, x+1, x+2, ... 52] -> [x, x+1, x+2, ... 52, 1, 2, 3, ... x-1]
# ache o ponto onde devemos cortar pra colocar de volta

deck = [i for i in range(1, 53)]
cut_example = 27
cut_deck = deck[27:] + deck[0: 27]

def deck_cut(deck):
    l = 0
    r = len(deck) - 1
    
    while r > l + 1:
        mid = (l + r) // 2
        if deck[l] > deck[mid]:
            r = mid
        elif deck[l] < deck[mid]:
            l = mid
            
    return l, r

print(deck_cut(cut_deck)) # 24, 25 -> 52, 1

# Tem outra forma de resolver o problema anterior
# como deck[0] é onde começa a segunda parte, faltam 52 - deck[0] para chegar na primera parte
# então é só cortar na posição deck[52-deck[0]]