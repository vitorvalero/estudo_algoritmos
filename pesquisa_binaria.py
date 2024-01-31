"""
A função a seguir realiza uma pesquisa binária em uma lista ordenada e retorna o índice do item, se encontrado.
Caso contrário, retorna None.

Args:
    lista (list): A lista ordenada onde a pesquisa será realizada.
    item: O item a ser pesquisado na lista.

Returns:
    int: O índice do item na lista, se encontrado. Caso contrário, retorna None.
"""

def pesquisa_binaria(lista, item):

    baixo = 0  # Define o índice mais baixo da lista
    alto = len(lista) - 1  # Define o índice mais alto da lista

    while baixo <= alto:  # Enquanto o índice mais baixo for menor ou igual ao índice mais alto
        meio = (baixo + alto) // 2  # Calcula o índice do meio da lista
        chute = lista[meio]  # Obtém o valor do item no índice do meio

        if chute == item:  # Se o valor do item for igual ao valor do chute
            return meio  # Retorna o índice do item
        elif chute > item:  # Se o valor do chute for maior que o valor do item
            alto = meio - 1  # Atualiza o índice mais alto para o índice anterior ao meio
        else:  # Se o valor do chute for menor que o valor do item
            baixo = meio + 1  # Atualiza o índice mais baixo para o índice posterior ao meio

    return None  # Retorna None se o item não for encontrado

minha_lista = [1, 3, 5, 7, 9]  # Lista ordenada para teste

print(pesquisa_binaria(minha_lista, 5))  # Realiza a pesquisa binária na lista e imprime o índice do item 5
print(pesquisa_binaria(minha_lista, -1))  # Realiza a pesquisa binária na lista e imprime None, pois o item -1 não está na lista
