import math
if __name__ == '__main__':
    vetor = []
    for i in range(5):
        while(True):
            try:
                vetor.append(int(input("Digite um inteiro: ")))
                break
            except ValueError:
                print("Valor invalido")
    print(sum(vetor))
    print(math.prod(vetor))
    print(vetor)