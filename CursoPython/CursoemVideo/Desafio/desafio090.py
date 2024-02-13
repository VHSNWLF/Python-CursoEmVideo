dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Media'] >= 6:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'
for k, v in dados.items():
    print(f'{k} é igual a {v}')
