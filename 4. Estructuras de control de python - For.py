#FOR: ciclo repetitivo de incrementos y decrementos,que va de un valor inicial a un valor final
#for range(v=solo un valor) - range(vi=valor inicial, vf=valor final) - range(vi, vf, incremento)
frase=input('Ingrese frase: ')
for indice in range(len(frase)):
    print(indice,'=',frase[indice])
#for in cadena - in (tupla) - in [lista]
for car in frase:
    if car in ('a','e','i','o','u','A','E','I','O','U'):
        if car in ['A','E','I','O','U']:
            continue
        else:
            cvoc = cvoc + 1
print('cantidad vocales:{}'.format(cvoc))
#Comprehension - [var for var in datos condicion]
[car for car in['a','e','i','o','u']if car not in('a','i','o')]