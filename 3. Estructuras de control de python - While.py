'''uso de while infinito'''
c = 1
while True:
    print(c)

#while validacion
vocal = input('ingrese vocal: ')
while vocal not in('a','e','i','o','u'):
    if vocal == '.':
        break
    vocal=input('Vocal: ')
print('Su vocal o punto es:{}'.format(vocal))

