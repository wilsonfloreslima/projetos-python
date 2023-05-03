from time import sleep
def mensagem(txt):
    print('--'*13)
    print(f' {txt:^12}')
    print('--'*13)

def fatorial1(num):
    fat = 1
    print('--'*12)
    for c in range(num, 0, -1):
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        sleep(0.5)
        fat *= c
    print(f'{fat}', end='')

def fatorial2(num):
    fat = 1
    print('--'*12)
    print(f'{num}! = ', end='')
    for c in range(num, 0, -1):
        fat *= c
    print(f'{fat}', end='')


#programa principal
mensagem('DIGITE UM VALOR INTEIRO!')
valor = int(input('Valor: '))
resp = int(input('1 ]Calculo passo a passo\n2 ]Resultado direto?\n : '))
while resp < 1 or resp > 2:
    resp = int(input('ERRO! 1 ]Calculo passo a passo\n2 ]Resultado direto?\n : '))
if resp == 1:
    fatorial1(valor)
if resp == 2:
    fatorial2(valor)
sleep(0.5)
print(' e.. FIM!')
mensagem(' FIM DE PROGRAMA')
