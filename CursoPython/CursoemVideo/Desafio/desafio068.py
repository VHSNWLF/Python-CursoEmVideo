import random
cont = flag = 0
while flag != 1:
    print("=" * 30)
    print("Vamos jogar Impar ou Par!")
    print("=" * 30)
    n = int(input("Escolha um numero: "))
    x = str(input("Impar ou Par? [I/P] ")).lower()
    comp = random.randint(0, 10)
    soma = n + comp
    print("O Computador escolheu {}".format(comp))
    if soma % 2 == 0 and x == "p":
        print("A soma deu {}. Deu Par, Você venceu!".format(soma))
        cont += 1
    elif soma % 2 == 0 and x != "p":
        print("A soma deu {}. Deu Par, Você perdeu!".format(soma))
        flag = 1
        break
    elif soma % 3 == 0 and x == "i":
        print("A soma deu {}. Deu Impar, Você Ganhou!".format(soma))
        cont += 1
    elif soma % 3 == 0 and x != "i":
        print("A soma deu {}. Deu Impar, Você perdeu!".format(soma))
        flag = 1
        break
print("GAME OVER! Você ganhou {} vezes".format(cont))
