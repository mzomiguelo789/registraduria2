Algoritmo calculadora
	
	Definir opc,a,b,resultado Como Real
	opc = 10
	resultado = 0
	Mientras opc <> 0 Hacer
	Escribir "escribe un numero"
	Leer a
	Escribir "escribe un numero"
	leer b
	escribir ""
	escribir "1=suma"
	Escribir "2=resta"
	Escribir "3=multiplicacion"
	Escribir "4=division"
	Escribir ""
	Escribir "elige una opcion"
	Leer opc
	Segun opc Hacer
		1:
			resultado = a+b
			Escribir "la suma de ",a," + ",b," = ",resultado
		2:
			resultado = a-b
			Escribir "la suma de ",a," - ",b," = ",resultado
		3:
			resultado = a*b
			Escribir "la multiplicacion de ",a," * ",b," = ",resultado
		4:
			resultado = a/b
			Escribir "la division de ",a," / ",b," = ",resultado
			
		De Otro Modo:
			Escribir  "sistema finalizado"
			opc = 0
	fin segun
FinMientras
	
	
FinAlgoritmo
