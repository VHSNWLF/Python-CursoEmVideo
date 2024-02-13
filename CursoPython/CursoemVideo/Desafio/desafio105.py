def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situação de varios alunos
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit == True:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# programa principal
resp = notas(5.5, 5.5, 9, 8.5, sit=True)
print(resp)
help(notas)



