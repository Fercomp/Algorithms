def compute_lps_array_optimized(pattern):
    """
    Calcula o Longest Proper Prefix which is also a Suffix (LPS) array 
    para o padrão P em tempo O(|P|).
    
    A lógica é semelhante ao próprio algoritmo KMP, mas compara o padrão consigo mesmo.
    """
    len_P = len(pattern)
    lps = [0] * len_P # Array para armazenar o LPS para cada prefixo
    
    # 'length' será o comprimento do prefixo próprio mais longo 
    # que também é um sufixo (LPS) para o prefixo anterior (i-1).
    length = 0 
    
    # 'i' é o índice atual que estamos construindo no array LPS.
    # lps[0] é sempre 0, então começamos em i = 1.
    i = 1       
    
    while i < len_P:
        if pattern[i] == pattern[length]:
            # CASO 1: Match
            # Encontramos um match, então o comprimento do LPS aumenta em 1.
            length += 1
            lps[i] = length
            i += 1
        else:
            # CASO 2: Mismatch
            # O caracter em pattern[i] não corresponde ao caracter em pattern[length].
            
            if length != 0:
                # Se 'length' não for zero, significa que há um prefixo/sufixo 
                # menor que podemos tentar usar.
                # Não voltamos length para 0; voltamos para o valor de LPS da 
                # posição anterior (length - 1). Isso é o que evita o O(|P|^2).
                length = lps[length - 1]
                # Nota: Não incrementamos 'i' aqui. O loop interno tentará 
                # comparar pattern[i] com o novo (menor) pattern[length].
            else:
                # Se 'length' for 0, não há prefixo/sufixo menor para tentar.
                # O LPS para o prefixo P[0...i] é 0.
                lps[i] = 0
                i += 1
                
    return lps

# Exemplos de uso:
P_1 = "ababa"
P_2 = "aabaaab"
P_3 = "abcdabd"

print(f"--- Cálculo Otimizado do Array LPS (O(|P|)) ---")
# P: 'a b a b a'
# LPS: 0 0 1 2 3 
print(f"P: '{P_1}' -> LPS: {compute_lps_array_optimized(P_1)}") 

# P: 'a a b a a a b'
# LPS: 0 1 0 1 2 2 3
print(f"P: '{P_2}' -> LPS: {compute_lps_array_optimized(P_2)}") 

# P: 'a b c d a b d'
# LPS: 0 0 0 0 1 2 0
print(f"P: '{P_3}' -> LPS: {compute_lps_array_optimized(P_3)}") 
print("-" * 30)

# A Magia por Trás da Otimização
# O segredo que torna este algoritmo linear está no tratamento do mismatch (mão-correspondência):
# Quando ocorre um mismatch em pattern[i] e pattern[length]:
# Versão Naive: Você reiniciaria a comparação do zero, checando se um prefixo de tamanho length - 1 coincide 
# com o sufixo de tamanho length - 1, e assim por diante (muito trabalho redundante!).

# Versão Otimizada (KMP):
# Sabemos que o prefixo P[0…length−1] já combinou com o sufixo P[i−length…i−1].
# Se não houve match em P[i], a próxima chance de ter um match (mantendo a parte da string já percorrida)
# deve ser usando o próximo prefixo mais curto que também é sufixo do segmento que falhou.
# Este comprimento é dado por lps[length - 1]. Ao fazer length = lps[length - 1], o KMP pula diretamente para
# o comprimento do próximo prefixo/sufixo mais longo que sabemos que já existe, sem nunca mudar o índice i.
# Ele só avança i quando encontra um match ou quando length chega a zero.
# Essa reutilização do conhecimento prévio sobre o próprio padrão é o que garante a eficiência O(∣P∣).