valor = float(input('qual o valor da casa'))
salario = float(input('qual o salario do comprador'))
anos = float(input('quantos anos sera parcelado'))
prestacao = valor/(anos*12)
if ( salario < (prestacao/100)*30 ):
    print('vc é pobre e vc n pode comprar uma casa')
else:
    print('serão {} por mes durante {} anos'.format(prestacao,anos))