n1 = int(input("Digite sua primeira nota:"))
n2 = int(input("Digite sua segunda nota:"))
media = (n1+n2)/2
if media <5:
    print(media)
    print("Reprovado")
elif 5 <= media <= 6.9:
    print(media)
    print("Recupeação")
else:
    print(media)
    print("Aprovado")