def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = chave

lista = []

i = 1
while i <= 10:
    elem = int(input("Digite um elemento da lista: "))
    lista.append(elem)
    i += 1

print("Lista antes da ordenação:", lista)

insertion_sort(lista)

print("Lista depois da ordenação:", lista)

