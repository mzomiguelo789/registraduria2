def categorias(tratamientoLista):
    nuevoTratamiento = []
    for t in tratamientoLista:
        nuevoTratamiento.append(t)
    return nuevoTratamiento

def mefaltandelacategoria(lista1, lista2, stringParam):
    salidaLista = []
    for index in lista1:
        value = lista2[index]
        if value == stringParam:
            salidaLista.append(index)
    return salidaLista

def notengopacientes(lista1, lista2):
    lista3 = []
    for i in lista1:
        if i not in lista2:
            lista3.append(i)
    return lista3

def puedecambiar(secundarioLista, primeroLista):
    cont = 0
    for i in secundarioLista:
        if i in primeroLista:
            cont = cont + 1
    return cont

