distancia = int(input('Qual foi a distância de sua viagem em Km: '))
if distancia<=200:
    total = distancia*0.50
    print('Você pagará 0,50R$ por Km andados, totalizando {:.2f}R$'.format(total))
else:
    total = distancia*0.45
    print('Você pagará 0,45R$ por Km andados, totalizando {:.2f}R$'.format(total))