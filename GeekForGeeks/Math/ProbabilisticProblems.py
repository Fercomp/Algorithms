''' Ω: Espaço amostral -> Conjunto de todos os possíveis resultados 
    F: Espaço de eventos -> Cada evento é um subconjunto do espaço amostral
    P: Funçao probabilidade -> Designia para cada possível evento uma probabilidade um valore real de 0 a 1
    
    Eventos mutualmente disjuntos tem a probabilidade dada pela soma das probabilidades
    Complemento de um evento é 1 - a probabilidade de A
    
    Axioma da inclusão/exclusão P(AUB) = P(A) U P(B) - P(A^B)
    Probabilidade condicional P(A|B) = P(A^B)/P(B)
    
    Esperança: Seja X uma variável com possíveis valores x1, x2, x3.. com possíveis probabilidades c1, c2, c3...
    a esperanca de X é a média ponderada de XxC
    
    Linearidade das esperanças: E[X + Y] = E[X] + E[Y], E[a.X] = a.E[X]
    a esperança de um dado de 6 lados é 3.5 e a de um de 20 é 10.5 logo a esperança de dois de 6 e um de 20 é 
    17.5
'''

# Cows and cars 