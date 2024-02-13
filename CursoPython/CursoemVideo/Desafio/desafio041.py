from datetime import date
AnodeNascimento = int(input("Digite o ano em que nasceu: "))
anoAtual = date.today().year
idade = anoAtual - AnodeNascimento
if idade <=9:
    print("Você é MIRIM")
elif idade <=14:
    print("Você é INFANTIL")
elif idade <=19:
    print("Você é JUNIOR")
elif idade <=20:
    print("Você é SÊNIOR")
elif idade >20:
    print("Você é MASTER")