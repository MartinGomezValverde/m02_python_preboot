from functools import reduce

def double(x):
    return x*2

lista = [1, 3, -1, 15, 9]

listaDouble = map(lambda x: x*2, lista) #El comando 'map' actúa con 'lambda' para cada ítem de la lista ( hace el doble de cada ítem ).
listaDouble1 = map(double, lista)

listaPares = filter(lambda x: x % 2 == 0, lista)

totalSum = reduce(lambda x, y: x + y, lista) #Reduce la lista a un sólo valor dependiendo de la función que se le implemente.

sum100 = reduce(lambda x, y: x + y, range(101))

sumDoubles = reduce(lambda x, y: x + y*2, lista)