#Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase.

frase=input("Frase: ")
cantidad=0
for x in frase:
    if x in "aeiou":
        cantidad+=1
print("Cantidad de vocales:", cantidad)


