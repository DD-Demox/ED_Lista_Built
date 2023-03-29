if __name__ == '__main__':
    print("Perguntas para achar o assasino")
    respostas = []
    while True:
        try:
            resposta = input("Telefonou para a vítima?S/N")
            if not (resposta.lower() == "s" or resposta.lower() == "n"):
                raise ValueError
            else:
                respostas.append(resposta.lower())
                break
        except ValueError:
            print("Valor invalido")
    while True:
        try:
            resposta = input("Esteve no local do crime?S/N")
            if not (resposta.lower() == "s" or resposta.lower() == "n"):
                raise ValueError
            else:
                respostas.append(resposta.lower())
                break
        except ValueError:
            print("Valor invalido")
    while True:
        try:
            resposta = input("Mora perto da vítima?S/N")
            if not (resposta.lower() == "s" or resposta.lower() == "n"):
                raise ValueError
            else:
                respostas.append(resposta.lower())
                break
        except ValueError:
            print("Valor invalido")
    while True:
        try:
            resposta = input("Devia para a vítima?S/N")
            if not (resposta.lower() == "s" or resposta.lower() == "n"):
                raise ValueError
            else:
                respostas.append(resposta.lower())
                break
        except ValueError:
            print("Valor invalido")
    while True:
        try:
            resposta = input("Já trabalhou com a vítima?S/N")
            if not (resposta.lower() == "s" or resposta.lower() == "n"):
                raise ValueError
            else:
                respostas.append(resposta.lower())
                break
        except ValueError:
            print("Valor invalido")
    contador = respostas.count("s")
    if contador == 5:
        print("ASSASSINO")
    elif contador >=3:
        print("Cumplice")
    elif contador >=2:
        print("Suspeito")
    else:
        print("Inocente")

