# 1) Pesquisa Binária

"""
    A pesquisa binária é um algoritmo que otimiza a busca da posição de um item em um array.
    Ela sempre "chutará" o número intermediário de itens do array
    E consequentemente elimina metade dos números restantes a cada chute
    Assim a quantidade de tentativas para descobrir um número será a menor possível
"""

def pesquisa_binaria(lista, item):
    """
    A função a seguir tem como parâmetros uma lista e um determinado item dessa lista
    E retorna o índice desse item
    """
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        #Utilizei o operador // para que seja retornada apenas a parte inteira da divisão 
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None     

minha_lista = [2, 5, 7, 16, 19]

print(pesquisa_binaria(minha_lista, 16)) # => 3 (índice 3)
