numeros = [2,37,49]

def mmc(numeros):
    max_ = max(numeros)
    i = 1
    while True:
        mult = max_ * i  #  Iremos pegar múltiplos do maior número
        if all(mult%x == 0 for x in numeros): #  Quando esse múltiplo for múltiplo dos outros valores da lista, irá retornar
            return mult # Retornará o primeiro valor no qual isso ocorre, logo o mmc.
        i += 1


final = 5000000
inicial = 1
qnt = (final-inicial)//mmc(numeros) # Calculando quantas vezes o mmc cabe no intervalo

print("Existem {} números entre {} e {} cumprindo tais requisitos. ".format(qnt,inicial,final))



