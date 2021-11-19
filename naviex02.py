from math import log

def fat(n):
    if n > 1:
        return n*fat(n-1)  # Utilizando que n! = n(n-1)!
    else:
        return 1

def bubbleSort(lista): #Função para ordenar em ordem crescente
    while True:
        trocas = 0
        for i in range(len(lista) - 1):
            if lista[i+1] < lista[i]:
                temp = lista[i] # Salvaremos o termo maior para fazermos as trocas
                lista[i] = lista[i+1] # Caso o termo sucessor seja menor, trocaremos ele com o termo anterior
                lista[i+1] = temp # Finalizando a troca
                trocas += 1
        if trocas == 0: break
    return lista



if __name__ == "__main__":


    # Criando o vetor com as posições pares e ímpares

    lista = [(3**i + 7*fat(i))*(abs(i%2 - 1)) + (2**i + 4*(log(i) if i>0 else 0))*(i%2) for i in range(10)]
    # O if i>0 else 0 é para evitar que tente calcular log(0) quando i=0.

    
    y = bubbleSort(lista) # Lista ordenada

    media = sum(lista)/len(lista)

    print("O maior elemento do vetor está na {}º posição e a média dos valores é: {:.2f} .".format(lista.index(y[-1])-1,media))