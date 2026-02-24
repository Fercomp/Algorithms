# https://leetcode.com/problems/insert-delete-getrandom-o1

import random

class RandomizedSet:
    # A ideia principal é usar um set para guardar os elementos, assim consigo
    # inserir e remover em O(1). O problema é que um set não permite acessar
    # elementos por índice, então não dá para escolher um elemento aleatório
    # diretamente com probabilidade uniforme.
    # A solução é usar um dicionário onde a chave é o valor inserido e o valor
    # é um índice que vai crescendo a cada inserção. Dessa forma, quando eu
    # for escolher algo aleatório, sei que o índice estará no intervalo
    # [1, elements_number].
    # Porém surge outro problema, temos um dicionário que mapeia valor -> índice,
    # mas para pegar o elemento sorteado precisamos acessar por índice.
    # Então usamos um segundo dicionário com o mapeamento inverso (índice -> valor).
    # Assim, quando geramos um índice aleatório, conseguimos recuperar
    # o valor correspondente em O(1).
    def __init__(self):
        self.values_set = {}
        self.indices_set = {}
        self.elements_number = 0

    # Verifico se já existe, se não eu adiciono tanto no indices_set quanto no values_set
    def insert(self, val: int) -> bool:
        if val in self.values_set:
            return False
        self.elements_number += 1
        self.indices_set[self.elements_number] = val
        self.values_set[val] = self.elements_number
        return True

    # Verifico se o valor existe. Se existir, pego o índice dele e também
    # pego o último elemento inserido (o de maior índice).
    # Então troco o último elemento para a posição do elemento que estamos removendo,
    # atualizando tanto o dicionário de índice -> valor quanto o de valor -> índice.
    # Por fim, removo o último elemento da estrutura e diminuo a contagem
    # de elements_number para manter os índices compactos.
    def remove(self, val: int) -> bool:
        if val not in self.values_set:
            return False
        val_index = self.values_set[val]
        max_value = self.indices_set[self.elements_number]
        max_index = self.values_set[max_value]

        self.indices_set[val_index] = max_value
        self.values_set[max_value] = val_index

        del self.values_set[val]
        del self.indices_set[max_index]

        self.elements_number -= 1
        return True

    def getRandom(self) -> int:
        i = random.randint(1, self.elements_number)
        return self.indices_set[i]