from datetime import date
maiores = 0
menores = 0
anoAtual = date.today().year
print(anoAtual)
for c in range (0,7):
    data = int(input("Digite o ano em que nasceu: "))
    idade = anoAtual - data
    if idade >=18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print("{} pessoas são maiores de idade. {} pessoas são menores de idade.".format(maiores,menores))