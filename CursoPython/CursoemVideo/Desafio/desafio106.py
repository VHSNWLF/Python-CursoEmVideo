def PyHelp(comando):
    print('\033[0;30;44m-=\033[m'*30)
    print(f'\033[0;30;44mAcessando o manual do comando [{comando}]\033[m')
    print('\033[0;30;44m-=\033[m' * 30)
    help(comando)


while True:
    print('\033[0;30;42m=\033[m'*30)
    print('\033[0;30;42mSistema de ajuda do PyHELP\033[m')
    print('\033[0;30;42m=\033[m'*30)
    com = str(input('Função ou Biblioteca > ').lower())
    if com == 'fim':
        break
    else:
        PyHelp(com)
