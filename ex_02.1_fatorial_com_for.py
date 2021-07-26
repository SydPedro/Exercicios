# Programa que calcula n!

n = int(input("Digite o número: "))
fatorial = 1
aux = 0

for i in range(1,n+1):
    fatorial = fatorial*i

print("O fatorial de", n, "é",fatorial)
