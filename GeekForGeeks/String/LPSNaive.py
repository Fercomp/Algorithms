# Count the longest proper prefix and sufix of an array is a essensial step
# in KMP algorithm fist we need to know what they are
# a proper prefix of a string is prefix that cannot be the full string,
# The same logic apply for sufix

# Proper prefix of "ABC"
# "", "A", "AB",

# Sufix of "ABC"
# "", "C", "BC", "ABC"

# Now we can construct an array of longest prefix and sufix of a string
# str = "ababc"
# arr = [0, 0, 1, 2, 0]
# i=0: "a"   -> LPS=0 (no proper prefix)
# i=1: "ab"  -> LPS=0
# i=2: "aba" -> LPS=1 ("a" is both P/S)
# i=3: "abab"-> LPS=2 ("ab" is both P/S)
# i=4: "ababc"-> LPS=0 

# str = "aaaa"
# arr = [0, 1, 2, 3]
# i=0: "a"   -> LPS=0
# i=1: "aa"  -> LPS=1 ("a")
# i=2: "aaa" -> LPS=2 ("aa")
# i=3: "aaaa"-> LPS=3 ("aaa")

# str "abcd"
# arr = [0, 0, 0, 0]
# i=0 to i=3: No character (other than the empty string) is repeated.


def get_lps_length_naive(prefix_string):
    """
    Calcula o comprimento do Longest Proper Prefix which is also a Suffix (LPS) 
    para uma dada string.

    Abordagem ingênua: itera sobre todos os comprimentos possíveis.
    
    Exemplo: prefixo_string = "ababa"
    - Comprimentos possíveis para checar: 4, 3, 2, 1.
    """
    n = len(prefix_string)
    # Lembre-se: o prefixo/sufixo deve ser *próprio*, então o comprimento máximo 
    # a ser checado é n - 1.
    
    # Tentamos comprimentos do maior para o menor (de n-1 até 1)
    for length in range(n - 1, 0, -1):
        # 1. Obter o prefixo de 'length'
        prefix = prefix_string[0:length]
        
        # 2. Obter o sufixo de 'length'
        # O sufixo de comprimento 'length' começa no índice n - length
        suffix = prefix_string[n - length:n]
        
        # 3. Comparar
        if prefix == suffix:
            # Encontramos o maior, podemos parar e retornar
            return length
            
    # Se nenhum prefixo/sufixo de comprimento > 0 for encontrado, o LPS é 0
    return 0

def fill_lps_naive(pattern):
    """
    Constrói o array LPS para o padrão usando a abordagem ingênua.
    
    O array LPS[i] armazena o LPS da substring P[0...i].
    
    Complexidade: O(|P|^3)
    - O loop principal roda |P| vezes.
    - O fatiamento da string (slicing) pode levar O(|P|) tempo.
    - O loop dentro de get_lps_length_naive leva O(|P|) tempo.
    """
    len_P = len(pattern)
    lps_array = [0] * len_P
    
    # O loop principal itera sobre cada índice 'i' do padrão
    for i in range(len_P):
        # O prefixo a ser analisado é P[0...i]
        current_prefix = pattern[0:i + 1]
        
        # Calculamos o LPS desse prefixo e armazenamos
        lps_array[i] = get_lps_length_naive(current_prefix)
        
    return lps_array