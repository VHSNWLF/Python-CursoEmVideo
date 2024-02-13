from time import sleep


def contador(inicio, fim, passo):
    if inicio > fim or passo < 0:
        print('-=' * 30)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim-1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-=' * 30)
    elif passo == 0:
        print('-=' * 30)
        print(f'Contagem de {inicio} até {fim} de 1 em 1')
        for c in range(inicio, fim):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-=' * 30)
    elif passo > 0:
        print('-=' * 30)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-=' * 30)

print('-=' * 30)
print(f'Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11):
    print(c, end=' ')

print('FIM!')
print('-='*30)
print(f'Contagem de 10 até 1 de 2 em 2')
for c in range(10, -1, -2):
    print(c, end=' ')

print('FIM!')
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
