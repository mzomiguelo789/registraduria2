nota_1 = float (input ('Ingresa el valor de nota 1: '))
nota_2 = float (input ('Ingresa el valor de nota 2: '))
nota_3 = float (input ('Ingresa el valor de nota 3: '))
promedio=(nota_1+nota_2+nota_3)/3
if promedio<3:
    print ('Reporbado')
else:
    print ('Aprobado')
print ('su promedio es de: ' + repr (promedio))
print ()

