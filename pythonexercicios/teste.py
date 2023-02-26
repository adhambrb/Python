from datetime import date
ano = int(input('digite que ano vc nasceu'))
mes = int(input('digite que mes vc nasceu'))
dia = int(input('digite que dia vc nasceu'))
nascimento = date(ano,mes,dia)
data_atual = date.today()

idade = nascimento.year - data_atual.year
if(nascimento.month > data_atual.month & nascimento.day > data_atual.day):

    idade = idade+1
    print('{}'.format(idade))
else:
    print('{}'.format(idade))

