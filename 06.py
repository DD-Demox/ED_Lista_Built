if __name__ == '__main__':
    media = []
    contadorMediaMaiorQue7 = 0
    for i in range(10):
        soma = 0.0
        mediaAluno = 0.0
        for j in range(4):
            while (True):
                try:
                    nota = float(input(f"Digite nota {j+1} para o(a) Aluno(a) {i+1}"))
                    if not 0 <= nota <= 10:
                        raise ValueError
                    soma = soma + nota
                    break
                except ValueError:
                    print("Valor invalido")
        mediaAluno = soma/4
        media.append((soma/4))
        if mediaAluno >= 7:
            contadorMediaMaiorQue7 += 1

    print(media)
    print(f"Tiveram {contadorMediaMaiorQue7} alunos com media maior ou igual a 7")
