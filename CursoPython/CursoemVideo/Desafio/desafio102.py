def fatorial(valor, show=False):
    """
    Calcula o fatorial de um numero
    :param valor: o numero a ser calculado
    :param show: parametro para mostrar todo o processo
    :return: O valor do fatorial de um numero 'Valor'
    """
    fat = valor
    c = valor - 1  # c=4
    while c != 0:
        fat = fat * c
        c -= 1
    if show:
        for c in range(valor, 0, -1):
            if c == 1:
                print(f'{c}', end=' ')
            else:
                print(f'{c} x', end=' ')
        return (f'= {fat}')
    else:
        return fat


# Programa principal
print(fatorial(5, show=True))
help(fatorial)
