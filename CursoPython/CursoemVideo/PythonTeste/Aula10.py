nome = str(input('qual é o seu nome: '))
if nome == 'Vitor':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão feio')
print('bom dia, {}!'.format(nome))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media>=6:
    print('{}, você passou de ano com a média {}'.format(nome,media))
else:
    print('{}, você não passou de ano com a média {}'.format(nome,media))