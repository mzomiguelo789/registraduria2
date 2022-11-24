#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, 
# el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
# El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
# Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y 
# el programa finalizará.



while True:
    print("Opción 1 - comenzar programa")
    print("Opción 2 - imprimir listado")
    print("Opción 3 - finalizar programa")
    opcion=int(input("Opción elegida: "))
    if opcion==1:
        print("¡Comenzamos!")
    elif opcion==2:
        print("Listado:")
        print("Nadia, Esteban, Mariela, Fernanda")
    elif opcion==3:
        print("Hasta la próxima")
        break
    else:
        print("Opción incorrecta. Debe ingresar 1, 2 o 3")

