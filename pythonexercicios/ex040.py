
n1 = float(input('digite a nota1'))
n2 = float(input('digite a nota2'))

m = (n1+n2)/2
if (m >= 7):
    print('aprovado')
elif(m>=5 & m<7):
    print('recuperacao')
else:
    print('reprovado')
