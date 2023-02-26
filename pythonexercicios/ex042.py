reta1 = int(input('digite o tamanho da reta'))
reta2 = int(input('digite o tamanho da reta'))
reta3 = int(input('digite o tamanho da reta'))
possivel = bool(True)

if (reta1+reta2>reta3 or reta1+reta3>reta2 or reta2+reta3 > reta1 ):
    print('da pra fzer um triangulo')
    

elif(possivel== True & reta1==reta2 & reta1==reta3 ):
    print('equilatero')
elif(reta1==reta2 or reta2==reta3 or reta3==reta1):
    print('isoceles')
elif(reta1!=reta2 & reta1!=reta3 & reta2!=reta3):
    print('escaleno')

else:
    print('nao da pra fazer triangulo')






