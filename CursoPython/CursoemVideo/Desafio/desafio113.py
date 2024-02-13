def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (TypeError, ValueError):
            print('ERRO: Por favor digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar o numero')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('ERRO: Por favor digite um número real válido.')
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar o numero')
            return 0
        else:
            return n


# Programa principal
n = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {n2}')