# Pedir para o usuário entrar o resultado de uma conta, ate acertar

resultado = 0;
while resultado != 12:
    resultado = int(input("Qual é o resultado de 2 x 6: "))
    if resultado == 12:
        print("Resposta correta!")
    else:
        print("Resposta errada, tente de novo...")
        print ("================================================")



