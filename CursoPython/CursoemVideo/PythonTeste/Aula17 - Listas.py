#===================================================================================================
#lista.append('Novo item')                                                                         }
#lista.insert(0, 'Novo item') / na posição 0                                                       }
#del lista[3]                                                                                      }
#lista.pop[3]                                                                                      }
#lista.pop / Elimina o último elemento                                                             }
#valores = list(range(4,11)) / Já cria uma lista com os valores em ordem, do 4 até o 10            }
#valores = [8,2,4,5,1,3,0] / n esta em ordem                                                       }
#valores.sort / Ordena os valores                                                                  }
#valores.sorte(reverse=True) / do maior para o menor                                               }
#===================================================================================================

num = [2,3,5,9]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop()
if 4 in num:
    num.remove(4)
else:
    print("Não achei o numero 4")
print(num)
print('Essa lista tem {} elementos'.format(len(num)))

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c,v in enumerate(valores):
    print('Na posição {} encontrei o valor {}!'.format(c,v))
print("Cheguei ao final da lista")

#valores2 = []
#for cont in range(0, 5):
 #   valores2.append(int(input('Digite um Valor: ')))
#print(valores2)

a = [2,4,6,7]
b = a
c = a[:]
b[2] = 10
print('Lista A: {} LISTA ORIGINAL'.format(a))
print('Lista B: {} LIGAÇÃO DA LISTA A'.format(b))
print('Lista C: {} CÓPIA DA LISTA A'.format(c))