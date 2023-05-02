from time import sleep

#colhendo dados
nome = str(input('Nome: '))
alt = float(input(f'Qual a altura de {nome}?[m] '))
peso = float(input(f'Qual o peso de {nome}?[kg] '))
print('Calculando, aguarde... ')
sleep(.5)
#calculo
imc = peso/(alt ** 2)
#definindo situação
if imc <= 18.5:
    stat = '\33[35;1mABAIXO DO IDEAL\33[m'
elif imc < 25:
    stat = '\33[32;1mIDEAL\33[m'
elif imc < 30:
    stat = '\33[34;1mSOBREPESO\33[m'
elif imc < 40:
    stat = '\33[31;1mOBESO\33[m'
else:
    stat = '\33[31;1mOBESIDADE MÓRBIDA\33[m'
#resultados
print('--'*12)
print(f' {nome} tem o IMC {imc:.1f}\n e sua situação é {stat}! ')
print('--'*12)
