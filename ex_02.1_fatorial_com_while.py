# Programa que calcula n!

n = int(input("Digite o número que deseja o fatorial: "))
fatorial = 1
aux = 0
while aux < n:
    fatorial = fatorial*(n-aux)
    aux = aux + 1
print("O fatorial de ", n, "é: ", fatorial)
