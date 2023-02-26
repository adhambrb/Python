peso  = float(input('digite seu peso em kg'))
altura = float(input('digite sua altura em metros'))

imc =  peso/(altura**2)
if imc < 18.5:
    print('seu imc é {:.2f} e voce esta abaixo do peso ideal'.format(imc))
elif imc>18.5 and imc<25:
    print('seu imc é {:.2f} e voce esta no peso ideal ! '.format(imc))
elif imc >25 and imc < 40:
    print('seu imc é {:.2f} e vc esta obeso'.format(imc))
elif imc > 40:
    print('seu imc é {:.2f} e vc esta com obesidade morbida'.format(imc))
else:
    print('algum erro ocorreu')