pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo [{pessoas["sexo"]}]')
print('-='*30)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='*30)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*30)
for k in pessoas.values():
    print(k)
print('-='*30)
for k in pessoas.keys():
    print(k)
print('-='*30)
##======================================================================================================================
##======================================================================================================================
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
##======================================================================================================================
##======================================================================================================================
brasil2 = list()
estadoo = dict()
for c in range(0, 3):
    estadoo['uf'] = str(input('Unidade Federativa: '))
    estadoo['sigla'] = str(input('Sigla do Estado: '))
    brasil2.append(estadoo.copy())
for e in brasil2:
    for v in e.values():
        print(v, end=' - ')
    print()