from statistics import mean
notas = []
for i in range(4):
    notas.append(float(input("Digite um nota:")))

print(notas)
print(mean(notas))

# ou
soma = sum(notas)
media = soma/len(notas)
print(format(media, ".2f"))