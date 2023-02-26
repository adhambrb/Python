numero = int(input('digite um numero'))
div = int(0)
for primo in range(2,numero+1):
    calc = numero%primo
    if calc == 0:
        div +=1

if div == 1:
        print(' {} é primo'.format(numero))
else:
        print('{} nao e primo'.format(numero))
