from time import sleep
#declaração de variáveis
pessoa = dict()
dados = list()
total = tothomem = totmulher = totidade = 0
while True:
    #armazenando dados em dicionários
    pessoa.clear()
    print('--'*8)
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['idade'] = int(input('Idade: '))
    totidade += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo[m/f]: ')).strip().upper()[0]
    #contador de homens
    if pessoa['sexo'] == 'M':
        tothomem += 1
    #contador de mulheres
    if pessoa['sexo'] == 'F':
        totmulher += 1
    #copiando dicionário para dentro de uma lista
    dados.append(pessoa.copy())
    #pessoas cadastradas
    total += 1
    resp = str(input('Cadastrar mais pessoas?[s/n] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('DADOS INVÁLIDOS! Cadastrar mais pessoas?[s/n] ')).upper().strip()[0]
    if resp == 'N':
        break
print('--'*15)
print('ORGANIZANDO DADOS, AGUARDE...')
sleep(1)
print('--'*15)
#mostrando lista com seus dicionários na tela
#cada indice da lista será um dicionário
print(f'{"NOME":5}\t{"IDADE":<8}\t\t{"SEXO":>2}')
print('--'*15)
for p in dados:
    print(f'{p["nome"]:<5}\t{p["idade"]:<8}\t\t{p["sexo"]:>2}')
print('--'*15)
print(f'Pessoas cadastradas: {total}')
print(f'Média de idade do grupo: {(totidade/total)}')
print(f'Mulheres cadastradas: {totmulher}')
print(f'Homens cadastrados: {tothomem}')
