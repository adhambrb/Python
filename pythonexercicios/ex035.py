reta1 = int(input('digite o tamanho da reta'))
reta2 = int(input('digite o tamanho da reta'))
reta3 = int(input('digite o tamanho da reta'))
if (reta1+reta2>reta3 or reta1+reta3>reta2 or reta2+reta3 > reta1 ):
    print('da pra fzer um triangulo')
else:
    print('nao da pr fazer triangulo')