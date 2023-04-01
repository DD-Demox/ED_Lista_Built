import statistics as s

if __name__ == '__main__':
    valores = []
    valoresAcimaMedia = []
    valoresAbaixoSete = []
    mediaCalculada = 0
    while True:
        try:
            valor = float(input("Digite um valor"))
            if valor > 10 or valor <-1:
                raise ValueError
            elif valor == -1:
                break
            else:
                valores.append(valor)
        except ValueError:
            print("Valor invalido")

    print(f"Foram lidas {len(valores)} notas")
    print(valores)
    for i in range(0,len(valores),-1):
        print(valores[i])
    print(sum(valores))
    mediaCalculada = s.mean(valores)
    print(mediaCalculada)
    for valor in valores:
        if valor > mediaCalculada:
            valoresAcimaMedia.append(valor)
        if valor < 7:
            valoresAbaixoSete.append(valor)
    print(f"A quantidade de notas acima da media é de {len(valoresAcimaMedia)}")
    print(f"A quantidade de notas abaixo de sete é de {len(valoresAbaixoSete)}")


