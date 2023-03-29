if __name__ == '__main__':
    vetor = []
    par = []
    impar = []
    for i in range(20):
        while(True):
            try:
                vetor.append(int(input(f"Digite numero {i+1}")))
                if vetor[-1] % 2 == 0:
                    par.append(vetor[-1])
                else:
                    impar.append(vetor[-1])
                break
            except ValueError:
                print("Valor invalido")

    print(vetor)
    print(par)
    print(impar)