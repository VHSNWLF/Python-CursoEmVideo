n1 = int(input("Digite um numero inteiro: "))
opcao = int(input("ESCOLHA UMA OPÇÃO\n[1]Binário\n[2]Octal\n[3]Hexadecimal\n"))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(n1, bin(n1)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n1, oct(n1)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n1, hex(n1)))
else:
    print("Opção inválida")