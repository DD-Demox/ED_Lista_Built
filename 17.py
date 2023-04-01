import statistics as s

if __name__ == '__main__':
    nomeclatura = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
    while True:
        nome = input("Atleta: ")
        saltos = []
        if nome == "":
            break
        for i in range(5):
            while True:
                try:
                    salto = input(f"{nomeclatura[i]} Salto: ")
                    salto=salto.removesuffix(" m")
                    salto=salto.removesuffix("m")
                    salto = float(salto)
                    saltos.append(salto)
                    break
                except ValueError:
                    print("Valor invalido")
        print(f"Atleta: {nome}")
        print(f"Saltos: {saltos}")
        print(f"Média dos saltos: {s.mean(saltos)} m")
    print("Fim do programa")