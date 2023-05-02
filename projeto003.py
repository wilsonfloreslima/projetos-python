from time import sleep
#inicialização de variáveis
total = 0
dados = []
lista = []
while True:
    #coletando dados
    print('--' * 12)
    nome = str(input('Nome: '))
    alt = float(input(f'Qual a altura de {nome}?[m] '))
    peso = float(input(f'Qual o peso de {nome}?[kg] '))
    #cálculo
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
    total += 1          #total de pessoas cadastradas
    dados.append(nome)      #dados[0]
    dados.append(imc)       #dados[1]
    dados.append(stat)      #dados[2]
    lista.append(dados[:])  #cópia de dados[] para lista[]
    dados.clear()
    resp = str(input('Deseja cadastrar mais pessoas?[s/n] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('DADOS INVÁLIDOS! Cadastrar mais pessoas?[s/n] ')).upper().strip()[0]
    if resp == 'N':
        break
#resultados
print('Aguarde... ')
sleep(0.5)
print('--'*20)
print(f'{ "RESULTADOS":^40}')
print(f'Foram cadastradas ao todo \33[34;1m{total}\33[m pessoa(s)!')
print('--'*20)
print(f'{"| NOME |":<5} {"| IMC |":<8} {"| SITUAÇÃO |":>8}')
print('--'*20)
for p in lista:
    print(f'{p[0]:<5} {p[1]:<8.1f} {p[2]:>8}')
print('--'*20)
