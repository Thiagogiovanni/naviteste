

def LeiaNota(msg):  # Criando uma função para validar o valores posteriormente inseridos
    ok = False
    nota = 0
    while True:
        nt = str((input(msg)))
        if nt.replace('.', '').isnumeric(): # Caso o valor tenha "." iremos por enquanto tira-lo e avaliar o resto do número
                                            # Caso o resto do valor seja numérico, vamos prosseguir e iremos parar o "While"
            nota = float(nt)
            ok = True
            break

        elif nt.replace(',', '').isnumeric(): # Mesma ideia do anterior
            nt = float(nt.replace(',','.'))  # Caso o valor inserido seja numérico (tirando a ","), iremos trocar essa , para um .


            ok = True

            return(float((nt)))

        else:
            print("Digite uma nota válida. ")

    return(float(nt))

if __name__ == "__main__":



    dicionario = {}


    for i in range(5):

        nome = "aluno" + str(i+1) # Denotaremos os alunos pelas suas "Posições", pois se pede, apenas,  que leia a nota.
        nota = LeiaNota("Digite a nota do {}º aluno: ".format(i+1))


        dicionario[nome] = nota


    ordem = sorted(dicionario.items(), key=lambda x: x[1])  # Ordenando o dicionario pelas notas (crescente)


    print("O aluno com a maior nota é o {}, sendo ela igual a {}".format(ordem[-1][0],ordem[-1][1]))



