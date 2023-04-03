def porcentagemJogador(numVotos:int,totalVotos:int):
    return (numVotos/totalVotos) * 100


if __name__ == '__main__':
    print("Enquete: Quem foi o melhor jogador?")
    votosComputados = [0 for i in range(23)]
    porcentagensJogador = [0 for i in range(23)]
    votosZeros = 0
    # votos, porcentagem, camisa
    votosValidos = []
    while True:
        try:
            numJogador = int(input("Número do jogador (0=fim): "))
            if numJogador > 23 or numJogador < 0:
                raise ValueError
            if numJogador == 0:
                break
            votosComputados[numJogador-1] += 1
        except ValueError:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
    totalVotos = sum(votosComputados)
    for i in range(len(votosComputados)):
        if votosComputados[i] == 0:
            continue
        else:
            porcentagensJogador[i] = round(porcentagemJogador(votosComputados[i],totalVotos),2)
            votosValidos.append([votosComputados[i], porcentagensJogador[i], (i+1)])
    votosValidos.sort(reverse=True)
    with open("enquete.txt","w") as enquete:
        enquete.write("Resultado da votação:")
        enquete.write("\n")
        enquete.write(f"Foram computados {totalVotos} votos.")
        enquete.write("\n")
        enquete.write("Jogador    Votos       %")
        enquete.write("\n")
        for i in range(len(votosValidos)):
            enquete.write(f"{votosValidos[i][2]}           {votosValidos[i][0]}           {votosValidos[i][1]}%")
            enquete.write("\n")

        enquete.write(f"O melhor jogador foi o número {votosValidos[0][2]}, com {votosValidos[0][0]} votos, correspondendo a {votosValidos[0][1]}% do total de votos.")





