def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e seu tamanho é de {tam}')


def soma(a, b):
    print(f'A = {a}')
    print(f'B = {b}')
    s = a + b
    print(f'A soma entre A + B = {s}')
    print('-='*30)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


#Programa Principal
soma(b=4, a=3)
soma(4, 5)
contador(2, 1, 7)
valores = [6, 3, 5, 10, 33]
print(valores)
dobra(valores)
soma2(2, 5, 7)

