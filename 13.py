import statistics

if __name__ == '__main__':
    listaMes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
                "Novembro", "Dezembro"]
    listaMediaTemperatura = []

    for i in range(12):
        listaMediaTemperatura.append(float(input(f"Qual a media de temp do mes de {listaMes[i]}")))

    mediaTemp = statistics.mean(listaMediaTemperatura)
    stringFinal = ""
    for i in range(12):
        if listaMediaTemperatura[i] > mediaTemp:
            stringFinal += f"{i+1} - {listaMes[i]}, "
    if stringFinal == "":
        print("Tudo Igual")
    else:
        stringFinal = "Os seguintes meses tiveram media maior que a media anual: " + stringFinal
        virgulaFinal = stringFinal.rindex(", ")
        stringFinal = stringFinal[:virgulaFinal]
        stringFinal += "."
        virgulaFinal = stringFinal.rindex(", ")
        stringFinal = stringFinal[:virgulaFinal]+" e "+stringFinal[virgulaFinal+2:]
    print(stringFinal)
