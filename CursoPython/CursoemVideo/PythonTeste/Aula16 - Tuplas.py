lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:]) #Suco, Pizza, Pudim
print(lanche[1:3]) #Suco, Pizza
print(lanche[-2]) #Pizza
print(lanche[:2]) #hamburguer, suco
print(lanche)#Todos
#Tuplas são imutaveis
#lanche[1] = 'Refrigerante'   #ERRO

for comida in lanche:
    print('Eu vou comer {}'.format(comida))

for cont in range(0, len(lanche)):
    print('Eu vou comer {} na posição {}'.format(lanche[cont], cont))

for pos, comida in enumerate(lanche):
    print('Eu vou comer {} na posição {}'.format(comida, pos))

print('Comi pra caramba')

print(sorted(lanche)) #Ordenado
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) #2,5,4,5,8,1,2
print(c.index(5, 1))

pessoa = 'Gustavo', 33, 'M', 99.88
del(pessoa)
print(pessoa)

