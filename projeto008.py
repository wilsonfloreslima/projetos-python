from time import sleep
#*referência global de cores
c = (
    '\33[m',        #0 - sem cor
    '\33[0;30;41m', #1 - vermelho
    '\33[0;30;42m', #2 - verde
    '\33[0;30;44m', #3 - azul
    '\33[7;40m',    #4 - branco
)
def titulo(txt, cor=0):
    tam = len(txt) + 2
    print(c[cor], end='')
    print('='*tam)
    print(f' {txt}')
    print('='*tam)
    print(c[0], end='')
    sleep(0.8)

def comando(ajuda):
    '''
    -> programa simulará um "mini-sistema" para utilização do comando 'help'
    :param ajuda: pesquisa que vir-a do escopo principal
    :return: não retornará dados
    '''
    titulo(f'Acessando o manual do comando {ajuda}, aguarde... ', 3) #texto com a cor azul(3)
    sleep(1)
    print(c[4], end='')
    help(ajuda)
    print(c[4], end='')
    sleep(1)


#programa principal
leia = ''
while True:
    titulo('>>>Digite um comando[Para sair, digite FIM]: ', 2) #texto com formatação na cor verde
    leia = str(input('>>> '))
    if leia in 'fimFIM':
        break
    else:
        comando(leia)
titulo('Processo encerrado! Obrigado por utilizar nossa plataforma.', 1) # texto com formatação na cor vermelha
