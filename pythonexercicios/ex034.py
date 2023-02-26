salario = float(input('digite seu salario'))
if (salario > 1250):
    aumento = (salario + (salario/100)*10)
    print('seu salario sera aumentado de {} para {}'.format(salario,aumento))
else:
    aumento = (salario + (salario/100)*15)
    print('recebera aumento de {} para {}'.format(salario,aumento))