frase = 'Vitor é um lindao'
print(frase)
print(frase[3])
print(frase[3:10])
print(frase[:10])
print(frase[10:])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(frase.replace('Vitor','Zé curubu'))
print("Vitor" in frase)
print(frase.find('Vitor'))
dividido = frase.split()
print(dividido)
print(dividido[3])
print(dividido[3][3])
print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(), strip(), junção com join().""")