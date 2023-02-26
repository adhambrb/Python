from datetime import date

pessoa = 7
for pessoa in range (1,7):
    ano = int(input('digite que ano vc nasceu'))
    mes = int(input('digite que mes vc nasceu'))
    dia = int(input('digite que dia vc nasceu'))
    nascimento = date(ano, mes, dia)
    data_atual = date.today()

    idade = data_atual.year - nascimento.year

    if idade <= 17:
        print('vc é menor de idade bro')
    else:
        print('vc é maior de idade')


