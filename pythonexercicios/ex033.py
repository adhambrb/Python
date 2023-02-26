n1 = int(input('numero1'))
n2 = int(input('numero2'))
n3 = int(input('numero3'))
if(n1>n2 & n1>n3):
    print('{} e o maior numero'.format(n1))
elif(n2>n1 & n2>n3):
    print('{} e o maior numero'.format(n2))
else:
    print('{} e o maior numero'.format(n3))
