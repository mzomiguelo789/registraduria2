
ingeniero = 2500000
arquitecto = 2100000
secretaria = 1200000
auxiliar = 1100000
operacion = int(input(" Seleccione una categoria: 1. Ingenieros, 2. Arquitectos, 3. Secretaria, 4. Auxiliar "))

if operacion == 1:
    resultado = ingeniero * 0.02 + ingeniero
    resultado2 = '{:,}'.format(resultado)
    print("su sueldo es", resultado2)
elif operacion == 2:
    resultado = arquitecto * 0.03 + arquitecto
    resultado2 = '{:,}'.format(resultado)
    print("su sueldo es", resultado2)
elif operacion == 3:
    resultado = secretaria * 0.04 + secretaria
    resultado2 = '{:,}'.format(resultado)
    print("su sueldo es", resultado2)
elif operacion == 4:
    resultado = auxiliar * 0.05 + auxiliar
    resultado2 = '{:,}'.format(resultado)
    print("su sueldo es", resultado2)
elif operacion >= 5:
    print(" Opcion incorrecta inicie de nuevo ")
