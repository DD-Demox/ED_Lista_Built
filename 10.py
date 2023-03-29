import random


def gerarVetor(tamanho=10):
    vetor = [random.randint(0, 100) for i in range(tamanho)]
    return vetor

if __name__ == '__main__':
    vetor1 = gerarVetor()
    vetor2 = gerarVetor()
    vetor3= []
    print(vetor1)
    print(vetor2)

    for i in range(10):
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])

    print(vetor3)

