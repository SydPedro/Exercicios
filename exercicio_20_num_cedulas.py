# programa que determina quais notas serão entregues conforme o valor solicitado

valor = int(input('Qual valor você deseja sacar: R$ '))
cinquenta = valor // 50
vinte = (valor - cinquenta * 50) // 20
dez = (valor - cinquenta * 50 - vinte * 20) // 10
cinco = (valor - cinquenta * 50 - vinte * 20 - dez * 10) // 5
dois = (valor - cinquenta * 50 - vinte * 20 - dez * 10 - cinco * 5) // 2
if cinquenta != 0:
    print(f'Total de {cinquenta} cédulas de R$50,00, totalizando R$ {cinquenta * 50},00')
if vinte != 0:
    print(f'Total de {vinte} cédulas de R$20,00, totalizando R$ {vinte * 20},00')
if dez != 0:
    print(f'Total de {dez} cédulas de R$10,00, totalizando R$ {dez * 10},00')
if cinco != 0:
    print(f'Total de {cinco} cédulas de R$5,00, totalizando R$ {cinco * 5},00')
if dois != 0:
    print(f'Total de {dois} cédulas de R$2,00, totalizando R$ {dois * 2},00')
print(' ')
print('Confira suas cédulas e muito obrigado por utilizar nosso sistema!')
