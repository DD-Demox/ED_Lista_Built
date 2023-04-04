import statistics


def conversorByteToMega(byte:int):
    return round(byte * 9.5367431640625e-7, 2)

def porcentagem(valor, total):
    return round((valor/total)*100,2)


if __name__ == '__main__':
    usuarios = []
    espacoUsado = []

    with open("usuarios.txt","r") as arquivo:
        for linha in arquivo:
            linha = linha.removesuffix("\n")
            usuarios.append(linha[:16])
            espacoUsado.append(int(linha[16:]))

    for i in range(len(espacoUsado)):
        espacoUsado[i] = conversorByteToMega(espacoUsado[i])

    with open("relatorio.txt","w") as relatorio:
        relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
        relatorio.write("------------------------------------------------------------------------\n")
        relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n")
        for i in range(len(usuarios)):
            relatorio.write(f"{i+1}    ")
            relatorio.write(f"{usuarios[i]}")
            relatorio.write(f"{espacoUsado[i]} MB")
            relatorio.write(13*" ")
            relatorio.write(f"{porcentagem(espacoUsado[i],sum(espacoUsado))}%")
            relatorio.write("\n")
        relatorio.write("\n")
        relatorio.write(f"Espaço total ocupado: {round(sum(espacoUsado), 2)} MB\n")
        relatorio.write(f"Espaço medio ocupado: {round(statistics.mean(espacoUsado), 2)} MB\n")
