if __name__ == '__main__':
    carros = ["Fusca","Ferrari","Tesla","Hammer","Mitsubishi"]
    consumos = [10,8,100,4,16]
    custoGasolina = 2.25
    distancia = 1000

    for i in range(len(carros)):
        print(f"Veiculo {i+1}")
        print(f"Nome: {carros[i]}")
        print(f"Km por litro: {consumos[i]}")
    print("\nRelatorio Final")

    for i in range(len(carros)):
        consumo = distancia/consumos[i]
        print(f" {i+1} - {carros[i]}           -    {consumos[i]} -  {consumo:.1f} litros - R$ {consumo*custoGasolina:.2f}")
    print(f"O menor consumo é o {carros[consumos.index(max(consumos))]}")