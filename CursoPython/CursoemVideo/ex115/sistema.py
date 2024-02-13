from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExistem(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
        sleep(1)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo')
        sleep(1)
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida\033[m')
        sleep(2)
