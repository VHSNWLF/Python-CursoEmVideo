primo = 0
n = int(input("Digite um numero: "))
for c in range(1, n+1):
    if (n % c == 0):
        primo = primo + 1
if primo == 2:
    print("primo")
else:
    print("não primo")
