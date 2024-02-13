
import random

n1 = int(input("[1]Pedra\n[2]Papel\n[3]Tesoura\n"))
n2 = random.randint(1,3)
#1 = pedra
#2 = papel
#3 = tesoura
if n1 == 1 and n2 == 1:
    print("Você: Pedra\nComputador: Pedra\nEMPATE.")
elif n1 == 1 and n2 == 2:
    print("Você: Pedra\nComputador: Papel\nVocê Perdeu.")
elif n1 == 1 and n2 == 3:
    print("Você: Pedra\nComputador: Tesoura\nVocê Ganhou.")
elif n1 == 2 and n2 == 1:
    print("Você: Papel\nComputador: Pedra\nVocê Ganhou.")
elif n1 == 2 and n2 == 2:
    print("Você: Papel\nComputador: Papel\nEMPATE.")
elif n1 == 2 and n2 == 3:
    print("Você: Papel\nComputador: Tesoura\nVocê perdeu.")
elif n1 == 3 and n2 == 1:
    print("Você: Tesoura\nComputador: Pedra\nVocê perdeu.")
elif n1 == 3 and n2 == 2:
    print("Você: Tesoura\nComputador: Papel\nVocê Ganhou.")
elif n1 == 3 and n2 == 3:
    print("Você: Tesoura\nComputador: Tesoura\nEMPATE.")
