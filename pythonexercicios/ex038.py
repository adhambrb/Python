n1 = int(input('digite um numero'))
n2 = int(input('digite um numero'))

if (n1 > n2 ):
    print('{} é o maior numero'.format(n1))
elif(n2>n1):
    print('{} é o maior numero'.format(n2))
else:
    print('{} e {} sao iguais'.format(n1,n2))