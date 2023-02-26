sexo = str(input('M/F?')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('informe corretamente M/F?')).strip().upper()[0]
print('sexo : {}'.format(sexo))