# Programa que decompoe um número em fatores primos

def primo(n):
    e_primo = True
    for i in range(2, n):
        if n % i == 0:
            e_primo = False
        if e_primo == False:
            break

    return (e_primo)


fatores = []

n = int(input("Digite o número para decompor: "))
n_ = n

for i in range(2, n + 1):
    if primo(i) == True:
        while n_ % i == 0:
            fatores.append(i)
            n_ = n_ / i;

print(fatores)
