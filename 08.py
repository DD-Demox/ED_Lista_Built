if __name__ == '__main__':
    altura = []
    idade = []
    for i in range(5):
        while True:
            try:
                altura.append(float(input(f"Digite a altura da pessoa {i+1}: ")))
                idade.append(int(input(f"Digite a idade da pessoa {i+1}: ")))
                break
            except ValueError:
                if len(altura) > (i+1):
                    altura.pop()
                print("Valor invalido")
    print(altura)
    print(idade)
    for i in range(4,-1,-1):
        print(f"Altura: {altura[i]}", end=" ")
        print(f"Idade: {idade[i]}")
