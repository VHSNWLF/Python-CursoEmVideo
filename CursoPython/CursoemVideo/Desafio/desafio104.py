def leiaInt(txt):
    ok = False
    valor= 0
    while True:
        n = str(input(txt))
        if n.isalnum():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de  digitar o numero {n}')