# https://vjudge.net/problem/UVA-170

from collections import deque

while True:
    deck = []
    # Optei por ler as 4 linhas em 4 variávies sem loop, porque eu preciso ler a primeira
    # para ver se não é o fim, se eu usasse o loop teria que ficar tratando quando i = 0,
    # mas poderia também
    line1 = input().split()
    if line1[0] == "#":
        break
    line2 = input().split()
    line3 = input().split()
    line4 = input().split()
    # concatenação de listas em python seguindo a ordem do input
    deck += line1 + line2 + line3 + line4
    # reversed múda a lista inplace preciso inverter porque ele fala no enunciado que a última 
    # do input é a primeira a ser jogada
    deck.reverse()
    # tive que criar um vetor com ordens porque não segue ordem alfabética ou númerica
    order_piles = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    # iniciar um deque pra cada pilha de forma que a chave é a o valor 
    piles = {r: deque() for r in order_piles} 

    # vou percorrendo todo o baralho (52 cartas 13 * 4), uso operação modular pra quando acabar 
    # o order_piles começar de novo, %13 pq o resto do 13 é 0 então ele vai pra primeira pilha
    for i in range(len(deck)):
        piles[order_piles[i % 13]].append(deck[i])

    # Aqui é a lógica princiapl, pega a primera cur, depois fica vendo se essa pilha não está vazia
    # se está acabou, se não insere cur embaixo e cur vira o top da pilha
    current_card = piles["K"].pop()
    cards_exposed = 1
    while True:
        rank = current_card[0]
        if len(piles[rank]) == 0:
            break
        current_card = piles[rank].pop()
        cards_exposed += 1

    # Aqui ele fala que cards exposed tem que ter dois dígitos mesmo quando é 1 até 9,
    # ficando 01, 02 ... eu usei o :02d que completa com 0 até 2 dígitos pra direita
    print(f"{cards_exposed:02d}, {current_card}")