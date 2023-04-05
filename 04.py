def eh_vogal(letra:str):
    letra = letra.lower()
    vogal=["a","e","i","o",'u']
    if letra in vogal:
        return True
    else:
        return False


if __name__ == '__main__':

    vetor=[]
    consoantes = []

    soma = 0
    for i in range(10):
        vetor.append(input("Digite um char"))

    for i in vetor:
        if not eh_vogal(i):
            soma += 1
            consoantes.append(i)


    print(soma)
    print(consoantes)
