if __name__ == '__main__':
    sistemasOps = ["Windows Server","Unix","Linux", "Netware","Mac OS","Outro"]
    votos = [0 for i in range(6)]
    while True:
        try:
            print("Qual o melhor Sistema Operacional para uso em servidores?")
            print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro")
            voto = int(input())
            if voto>6 or voto<0:
                raise ValueError
            elif voto == 0:
                break
            else:
                votos[voto-1] += 1
        except ValueError:
            print("Valor invalido")
    votosTotais = sum(votos)
    print("Sistema Operacional     Votos   %")
    print("-------------------     -----   ---")
    for i in range(6):
        espaçoBranco = 25-len(sistemasOps[i])
        print(sistemasOps[i]+espaçoBranco*" " + str(votos[i]) + "      " + str(round(((votos[i]/votosTotais)*100), 2)) + "%")

    print("-------------------     -----")
    print(f"Total                    {votosTotais}\n")
    indexMaior = votos.index(max(votos))
    print(f"O Sistema Operacional mais votado foi o {sistemasOps[indexMaior]}, com {votos[indexMaior]} votos, correspondendo a {round(((votos[indexMaior]/votosTotais)*100), 2)}% dos votos.")
