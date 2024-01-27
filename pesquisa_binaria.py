# Cria a função de pesquisa binária, com seus argumentos "lista" e "item":
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    # While loop que realiza a pesquisa binária até localizar e retornar a posição do argumento "item" na lista:
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
            
    # Caso o valor do argumento "item" não esteja contido no conjunto do argumento "lista", retorna "None":
    else:
        return None


# Teste da função de pesquisa binária:
minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 5))
print(pesquisa_binaria(minha_lista, -1))
