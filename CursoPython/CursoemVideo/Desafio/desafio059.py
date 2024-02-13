n1 = int(input("Digite seu primeiro valor: "))
n2 = int(input("Digite seu segundo valor: "))
n = 0
while n != 5:
    n = int(input("[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Numeros\n[5]Sair do Programa\n"))
    if n == 1:
        soma = n1+n2
        print("Soma: {}".format(soma))
    elif n == 2:
        mult = n1 * n2
        print("Multiplicação: {}".format(mult))
    elif n == 3:
        if n1>n2:
            print("Maior: {}".format(n1))
        else:
            print("Maior: {}".format(n2))
    elif n == 4:
        n1 = int(input("Digite seu primeiro valor: "))
        n2 = int(input("Digite seu segundo valor: "))
    elif n == 5:
        n = 5
    else:
        print("Comando inválido")
print("FIM")
