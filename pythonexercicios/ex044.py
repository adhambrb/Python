from random import randint
itens = ('pedra','papel','tesoura')
computador  =  randint (0,2)
print('''Escolha sua opção 
[0] PEDRA
[1] PAPEL
[2] TESOURA     ''')
print('*--*--'*15)
jogador = int(input('pressione o numero correspondente a sua escolha'))
print('o computador escolheu {}'.format(itens[computador]))
print('o jogador escolheu {}'.format(itens[jogador]))
print('*--*--'*15)
if computador  == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCEU')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU')
    else:
        print('jogada invalida')
if computador  == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O JOGADOR VENCEU')
    else:
        print('jogada invalida')
if computador  == 2:
    if jogador == 0:
        print('O JOGADOR VENCEU')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('jogada invalida')




