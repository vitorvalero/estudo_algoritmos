"""
A função a seguir encontra o menor elemento em uma lista.

Args:
    lista (list): A lista de elementos.

Returns:
    int: O índice do menor elemento na lista.
"""

def busca_menor(lista):
    menor = lista[0]  # Define o primeiro elemento da lista como o menor
    menor_indice = 0  # Define o índice do menor elemento como 0
    
    for i in range(1, len(lista)):
        if lista[i] < menor:  # Verifica se o elemento atual é menor que o menor encontrado até agora
            menor = lista[i]  # Atualiza o menor elemento
            menor_indice = i  # Atualiza o índice do menor elemento
    
    return menor_indice


"""
A função a seguir realiza a ordenação por seleção em uma lista.

Args:
    lista (list): A lista de elementos a ser ordenada.

Returns:
    list: A lista ordenada.
"""

def ordenacao_selecao(lista):
    lista_ordenada = []

    for i in range(len(lista)):
        menor = busca_menor(lista)  # Encontra o menor elemento da lista
        lista_ordenada.append(lista.pop(menor))  # Remove o menor elemento da lista e adiciona à lista ordenada
    
    return lista_ordenada

minha_lista = [3, 9, 1, 4, 6, 8]

print(ordenacao_selecao(minha_lista))  # Imprime a lista ordenada
