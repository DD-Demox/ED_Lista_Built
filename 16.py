import random


class Vendedor:
    def __init__(self, vendas):
        self.salarioBase = 200
        self.salarioReal = 0
        self.vendas = round(vendas,2)

    def calcularSalarioReal(self):
        self.salarioReal = round(self.salarioBase + (self.vendas * 0.09),2)

    def getSalarioReal(self):
        return self.salarioReal


if __name__ == '__main__':
    vendedores = []
    contadores = [0 for i in range(9)]
    for i in range(10):
        vendedor = Vendedor(random.uniform(0,10000))
        vendedores.append(vendedor)
    for vendedor in vendedores:
        vendedor.calcularSalarioReal()
        print(f"{vendedor.getSalarioReal()}",end=" ")
        posicao = int(vendedor.getSalarioReal() // 100)
        if posicao >= 10:
            contadores[8] += 1
        else:
            contadores[posicao-2] += 1
    print()
    print(contadores)