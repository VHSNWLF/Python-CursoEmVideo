try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except KeyboardInterrupt:
    print('O usuario preferiu não digitar os daodos.')
except (ValueError, TypeError):
    print('Os tipos informados não correspondem')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero.')

except Exception as erro:
    print(f'O erro foi: {erro.__class__}')
else:
    print(f'Resultado: {r}')
finally:
    print('Volte sempre!')