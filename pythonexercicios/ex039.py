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
    if(idade == 18):
        print('vc precisa se alistar ao tiro de guerra ')
    elif(idade < 18 ):
        print('ainda faltam {} para seu alistamento'.format(18-idade))
    else:
        print('vc esta {} anos atrasado para o alistamento'.format(idade - 18))
