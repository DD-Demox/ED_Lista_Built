import math
if __name__ == '__main__':

    vetorA = []
    for i in range(10):
        while True:
            try:
                vetorA.append(int(input("Digite um inteiro: ")))
                break
            except ValueError:
                print("Valor invalido")

    vetorPOW = [i ** 2 for i in vetorA]
    print(vetorPOW)
    print(sum(vetorPOW))