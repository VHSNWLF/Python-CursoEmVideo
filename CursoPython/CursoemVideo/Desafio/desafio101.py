import datetime
def voto(ano):
    idade = datetime.date.today().year - ano
    if idade < 18:
        return (f'Com {idade} anos: Não vota')
    elif idade >=65:
        return (f'Com {idade} anos: Voto Opcional')
    elif idade >=18:
        return (f'Com {idade} anos: Voto Obrigatório')


anoNascimento = int(input('Ano em que nasceu: '))
print(voto(anoNascimento))