# Programa que verifica se um número é primo

def primo(n):
    e_primo = True
    for i in range(2, n):
        if n % i == 0:
            e_primo = False
        if e_primo == False:
            break

    return (e_primo)


n = int(input("Digite o número para verificar se é primo: "))

if primo(n) == True:
    print("O número", n, "é primo.")
else:
    print("O número", n, "não é primo.")
