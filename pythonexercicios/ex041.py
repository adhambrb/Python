from datetime import date
ano = int(input('digite que ano vc nasceu'))
mes = int(input('digite que mes vc nasceu'))
dia = int(input('digite que dia vc nasceu'))
nascimento = date(ano,mes,dia)
data_atual = date.today()

idade = data_atual.year - nascimento.year
if(nascimento.month > data_atual.month & nascimento.day > data_atual.day):

    idade = idade+1
    print('{}'.format(idade))

else:
    print('{}'.format(idade))
    if(idade < 10):
        print('mirim ')
    elif(idade < 15 ):
        print('infantil'.format(18-idade))
    elif(idade <= 19 ):
        print(' junior '.format(idade - 18))
    elif(idade == 20):
        print('senior')
    else:
        print('master')
