numero = int(input('digite um numero'))


menu = int(input('para binario digite 1 \n'
                 'para octal digite 2  \n'
                 'para hexadecimal digite 3\n'))


if (menu == 1) :
        print('{} convertido para binario  = {}'.format(numero,bin(numero)))
elif (menu == 2) :
        print('{} convretido para octal = {} '.format(numero,oct(numero)))
elif (menu == 3) :
        print('{} convertido para hexadecimal = {}'.format(numero,hex(numero)))
else:
        print('comando invalido, tente novamente')
