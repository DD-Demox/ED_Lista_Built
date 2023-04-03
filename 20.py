if __name__ == '__main__':
    salarios = []
    abonos = []
    while True:
        try:
            salario = round(float(input("Salario: ")),2)
            if salario > 0:
                salarios.append(salario)
                abono = round(salario * 0.2,2)
                if abono < 100:
                    abonos.append(100)
                else:
                    abonos.append(abono)
            elif salario == 0:
                break
            else:
                raise ValueError

        except ValueError:
            print("Valor invalido")
    print("Salário    - Abono")
    for i in range(len(salarios)):
        print(f"R$ {salarios[i]:.2f} - {abonos[i]:.2f}")
    print(f"Foram processados {len(salarios)} colaboradores")
    print(f"Total gasto com abonos: R$ {sum(abonos):.2f}")
    print(f"Valor mínimo pago a {abonos.count(100)} colaboradores")
    print(f"Maior valor de abono pago: R$ {max(abonos):.2f}")
