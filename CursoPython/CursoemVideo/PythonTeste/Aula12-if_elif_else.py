nome = str(input('Qual é o seu nome: '))
if nome == "Vitor":
    print("Que nome Lindo")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que lindo nome feminino')
else:
    print("seu nome é normal")
print('Tenha um bom dia, {}'.format(nome))