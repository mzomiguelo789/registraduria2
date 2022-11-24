#Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. 
# En cada iteración, solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números 
# ingresados.


c=int(input("Cantidad de números: "))
total=0
for variable in range(c):
   numero=int(input("Número: "))
   total+=numero
print("Total de la suma:", total)

