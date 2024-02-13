from datetime import date
dados = dict()
dados['Nome'] = str(input('Digite seu nome: '))
dados['AnoNascimento'] = int(input('Digite o ano em que nasceu: '))
dados['CarteiraTrabalho'] = int(input('Carteira de Trabalho: '))
if dados['CarteiraTrabalho'] != 0 :
    dados['AnoContratação'] = int(input('Qual foi o ano de contratação: '))
    dados['Salario'] = float(input('Qual seu salario: '))
    dados['Aposentadoria'] = (date.today().year - dados['AnoNascimento']) + ((dados['AnoContratação'] + 35) - date.today().year)
dados['AnoNascimento'] = date.today().year - dados['AnoNascimento']
print('-='*30)
for k,v in dados.items():
    if k == 'AnoNascimento':
        print(f'Idade tem o valor {v}')
    else:
        print(f'{k} tem o valor {v}')