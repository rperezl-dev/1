'''Funciones sin retorno'''
def vocales(frase):
    for car in frase:
        if car in('a','e','i','o','u'):
            print(car)

'''LLamada a funcion'''
oracion=input('ingrese oracion: ')
vocales(oracion.lower())
'''Funciones con retorno de valor'''
def promedio(notas):
    summ=0
    for n in notas:
        summ+=n #summ = summ + n
        return summ/len(notas)
#llamada a funcion
listanotas=[2,4,6,8,10]
prom=promedio((listanotas))
print('Promedio:{}={}'.format(listanotas,prom))


#funciones con retorno:con el valor se pretende hacer otra cosa.
#funciones sin retorno: no retorna nada.