from random import randint
from time import sleep
def mensagem(msg):
    print('--' * 8)
    print(f' {msg:^15}')
    print('--' * 8)

def jogo():
    resp = ''
    while True:
        jogador = int(input('Escolha:\n1] Pedra\n2] Papel \n3] Tesoura\n: '))
        while jogador < 1 or jogador > 3:
            jogador = int(input('DADOS INVÁLIDOS!Escolha:\n1] Pedra\n2] Papel \n3] Tesoura\n: '))
        com = randint(1, 3)
        print('JO.. ', end='')
        sleep(1)
        print('KEN.. ', end='')
        sleep(1)
        print('PÔ.. ')
        print('--' * 8)
        if com == jogador:
            print('Escolheram iguais!')
            print('NIGUEM VENCE!')
        else:
            if jogador == 1 and com == 2:
                print('\33[32mJOGADOR\33[m escolheu PEDRA, \33[31mCOM\33[m escolheu PAPEL.')
                print('\33[31;1mCOM VENCE!\33[m')
            elif jogador == 1 and com == 3:
                print('\33[32mJOGADOR\33[m escolheu PEDRA, \33[31mCOM\33[m escolheu TESOURA.')
                print('\33[32;1mJOGADOR VENCE!\33[m')
            elif jogador == 2 and com == 1:
                print('\33[32mJOGADOR\33[m escolheu PAPEL, \33[31mCOM\33[m escolheu PEDRA.')
                print('\33[32;1mJOGADOR VENCE!\33[m')
            elif jogador == 2 and com == 3:
                print('\33[32mJOGADOR\33[m escolheu PAPEL, \33[31mCOM\33[m escolheu TESOURA.')
                print('\33[31;1mCOM VENCE!\33[m')
            elif jogador == 3 and com == 1:
                print('\33[32mJOGADOR\33[m escolheu TESOURA, \33[31mCOM\33[m escolheu PEDRA.')
                print('\33[31;1mCOM VENCE!\33[m')
            elif jogador == 3 and com == 2:
                print('\33[32mJOGADOR\33[m escolheu TESOURA, \33[31mCOM\33[m escolheu PAPEL.')
                print('\33[32;1mJOGADOR VENCE!\33[m')
        print('--' * 8)
        resp = str(input('Deseja continuar?[s/n] ')).strip().upper()[0]
        if resp != 'SN':
            resp = str(input('ERRO! Deseja continuar?[s/n] ')).strip().upper()[0]
        if resp == 'N':
            break


#programa principal
mensagem('JO KEM PÔ')
jogo()
mensagem('FIM DE JOGO!')
