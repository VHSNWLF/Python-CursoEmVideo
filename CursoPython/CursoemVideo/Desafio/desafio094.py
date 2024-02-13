pessoa = dict()
pessoas = list()
mediaIdade = 0
listaMulheres = list()
listaAcimaIdade = list()

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ').upper()[0])
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    if pessoa['Sexo'] == 'F':
        listaMulheres.append(pessoa.copy())
    pessoas.append(pessoa.copy())
    while True:
        val = str(input('Quer continuar? [S/N] ').upper()[0])
        if val in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if val == 'N':
        break
    print('-='*30)

print('-='*30)

for i in pessoas:
    mediaIdade += i['Idade']
mediaIdade = mediaIdade/len(pessoas)

print(f'A quantidade de pessoas cadastradas foram de {len(pessoas)}. A média de idades é {mediaIdade}')
print(f'As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da média', end='')
for p in pessoas:
    if p['Idade']>= mediaIdade:
        print(f'{p["Nome"]}',end=' ')
print("<< ENCERRADO >>")