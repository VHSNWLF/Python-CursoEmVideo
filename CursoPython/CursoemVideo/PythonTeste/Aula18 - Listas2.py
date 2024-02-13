galera = [['Joao', 19],["Ana", 33],['Joaquim', 13],['Maria', 45]]
print(galera[1:])
for p in galera:
    print('{} tem {} anos de idade'.format(p[0], p[1]))

galera2 = list()
dado = list()
print('-'*30)
print('CADASTRO DE PESSOAS')
print('-'*30)
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
for p in galera2:
    if p[1] >= 18:
        print('{} é maior de idade'.format(p[0]))
    else:
        print('{} é menor de idade'.format(p[0]))