import random


def gerar_aluno():
    vetor = []
    vetor.append(random.randint(5,60))
    vetor.append(float(format(random.uniform(1,2),".2f")))
    return vetor


if __name__ == '__main__':
    alunos = []
    somaIdades = 0
    contador = 0
    for i in range(30):
        alunos.append(gerar_aluno())
    print(alunos)
    for i in alunos:
        somaIdades += i[1]
    mediaSoma = somaIdades/len(alunos)
    print(mediaSoma)
    for i in alunos:
        if i[0]>13 and i[1] < mediaSoma:
            contador += 1
    print(f"{contador} tem mais que 13 anos e estão abaixo da media de altura")



