from busquedas_02 import aestrella, ProblemaBusqueda
from timeit import default_timer

OBJETIVO = '''1-2-3
4-5-6
7-8-9
a-b-z'''

INICIAL = '''a-b-z
9-8-7
6-5-4
3-2-1'''

inicio = default_timer()

def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


def find_location(filas, element_to_find):
    '''Encuentra la ubicacion de una pieza en el rompecabezas.
       DEvuelve una tupla: fila, columna'''
    for ir, row in enumerate(filas):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


posiciones_objetivo = {}
filas_objetivo = string_to_list(OBJETIVO)
for numero in '123456789abz':
    posiciones_objetivo[numero] = find_location(filas_objetivo, numero)


class FourteenthPuzzleProblem(ProblemaBusqueda):
    def acciones(self, estado):
        '''Devuelve una lista de piesas que se pueden mover a un espacio vacio.'''
        filas = string_to_list(estado)
        fila_z, columna_z = find_location(filas, 'z')

        acciones = []
        if fila_z > 0:
            acciones.append(filas[fila_z - 1][columna_z])
        if fila_z < 3:
            acciones.append(filas[fila_z + 1][columna_z])
        if columna_z > 0:
            acciones.append(filas[fila_z][columna_z - 1])
        if columna_z < 2:
            acciones.append(filas[fila_z][columna_z + 1])

        return acciones

    def resultado(self, estado, accion):
        '''Devuelve el resultado despues de mover una pieza a un espacio en vacio
        '''
        filas = string_to_list(estado)
        fila_z, columna_z = find_location(filas, 'z')
        fila_n, columna_n = find_location(filas, accion)

        filas[fila_z][columna_z], filas[fila_n][columna_n] = filas[fila_n][columna_n], filas[fila_z][columna_z]

        return list_to_string(filas)

    def es_objetivo(self, estado):
        '''Devuelve True si un estado es el estado_objetivo.'''
        return estado == OBJETIVO

    def costo(self, estado1, accion, estado2):
        '''Devuelve el costo de ejecutar una accion. 
        '''
        return 1

    def heuristica(self, estado):
        '''Devuelve una estimacion de la distancia
        de un estado a otro, utilizando la distancia manhattan.
        '''
        filas = string_to_list(estado)

        distancia = 0

        for numero in '123456789abz':
            fila_n, columna_n = find_location(filas, numero)
            fila_n_objetivo, col_n_goal = posiciones_objetivo[numero]

            distancia += abs(fila_n - fila_n_objetivo) + abs(columna_n - col_n_goal)

        return distancia


resultado = aestrella(FourteenthPuzzleProblem(INICIAL))

for accion, estado in resultado.camino():
    print('Mueve la loceta', accion)
    print(estado)
fin = default_timer()
print((fin - inicio)/60,' Minutos')