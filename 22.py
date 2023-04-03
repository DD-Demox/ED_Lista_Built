if __name__ == '__main__':
    defeito = ["necessita da esfera","necessita de limpeza","necessita troca do cabo ou conector","quebrado ou inutilizado"]
    contadoresDefeitos = [0 for i in range(4)]
    mouses = []
    while True:
        try:
            id = input("Digite identificaçao do mouse")
            if id == "0":
                break
            print("Qual o problema do mouse?")
            for i in range(len(defeito)):
                print(f"{i+1} - {defeito[i]}")
            escolha = int(input())
            if 1<=escolha<=4:
                mouses.append([id,defeito[escolha-1]])
                contadoresDefeitos[escolha-1] +=1
            elif escolha == 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("Valor invalido")
    print("Relatorio")
    print(f"Quantidade de mouses: {len(mouses)}")
    print("Situação                        Quantidade              Percentual")
    contadoresDefeitosCopia = contadoresDefeitos
    for i in range(len(contadoresDefeitosCopia)):
        if max(contadoresDefeitosCopia) == 0:
            break
        indexMaxAtual = contadoresDefeitosCopia.index(max(contadoresDefeitosCopia))
        print(f"{i+1}- {defeito[indexMaxAtual]}"+(37-len(defeito[indexMaxAtual]))*" "+f"{contadoresDefeitosCopia[indexMaxAtual]}"+20*" "
              + f"{round(((contadoresDefeitosCopia[indexMaxAtual]/len(mouses))*100),2)}%")
        contadoresDefeitosCopia[indexMaxAtual] = 0
