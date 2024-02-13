maior = 0
menor = 999999
for c in range(0, 5):
    peso = float(input("Digite seu peso: "))
    if peso > maior:
        maior = peso
        if peso < menor:
            menor = peso
    elif peso < menor:
        menor = peso
print("O maior peso registrado foi: {}. O menor peso registrado foi {}.".format(maior, menor))