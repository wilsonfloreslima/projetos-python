from time import sleep
def mensagem(txt):
    print('--' * 10)
    print(f'{txt:^20}')
    print('--' * 10)

def progressiva(i, f, p = 1):
    '''
    --> contador crescente. Caso o valor inicial recebido for MENOR que o final.
    :param i: valor inicial do contador
    :param f: valor final do contador
    :param p: passo do contador.
    :return: não serão retornados valores
    '''
    print('--' * 10)
    print('INICIO:', end='')
    for c in range(i, f, p):
        print(f' {c}', end='')
        sleep(1)
    print(' e.. FIM!!!')

def regressiva(i, f, p = -1):
    '''
        --> contador decrescente. Caso o valor inicial recebido for MAIOR que o final.
        :param i: valor inicial do contador
        :param f: valor final do contador
        :param p: passo do contador.
        :return: não serão retornados valores
        '''
    print('--' * 10)
    print('INICIO:', end='')
    for c in range(i, f, p):
        print(f' {c}', end='')
        sleep(1)
    print(' e.. FIM!!!')


#programa principal
mensagem('CONTADOR SIMPLES')
inicio = int(input('Valor inicial do contador: '))
fim = int(input('Valor final do contador: '))
if inicio > fim:
    valor = int(input('Passo do contador: '))
    passo = valor * (-1)
    regressiva(inicio, fim, passo)
else:
    passo = int(input('Passo do contador: '))
    progressiva(inicio, fim, passo)
