from datetime import date
AnodeNascimento = int(input("Digite o ano em que nasceu: "))
anoAtual = date.today().year
idade = anoAtual - AnodeNascimento
if idade == 18:
    print("Deve realizar o alistamento esse ano")
elif idade > 18:
    print("Já passou do prazo")
    resto = idade - 18
    print("passou {} ano(s) do prazo".format(resto))
else:
    print("Ainda não devera realizar o alistamento")
    resto = 18 -idade
    print("faltam {} ano(s) para o alistamento".format(resto))