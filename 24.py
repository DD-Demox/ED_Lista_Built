import random

if __name__ == '__main__':
    dadosLancados = [random.randint(1, 6) for i in range(100)]
    contador = [0 for i in range(6)]
    for i in dadosLancados:
        contador[i-1] += 1

    print(contador)