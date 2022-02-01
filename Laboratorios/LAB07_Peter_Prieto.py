'''
Grupo 4
Alison Paola Jacko 
Peter Alejandro Prieto Cespedes
María Elena Ramos
Paulo Aldo Quispe
            

'''
import random
PM = 0
PC = 0
PP = 0
class Problema_Genetico(object):
    # Constructor
    def __init__(self, genes, fun_decodificar, fun_cruzar, fun_mutar, fun_fitness, longitud_individuos):
        self.genes = genes
        self.fun_decodificar = fun_decodificar
        self.fun_cruzar = fun_cruzar
        self.fun_mutar = fun_mutar
        self.fun_fitness = fun_fitness
        self.longitud_individuos = longitud_individuos
    
    def decodificar(self, genotipo):
        #Devuelve el fenotipo a partir del genotipo
        fenotipo = self.fun_decodificar(genotipo)
        return fenotipo
    
    def cruzar(self, cromosoma1, cromosoma2):         
        #Devuelve el cruce de un par de cromosomas
        cruce = self.fun_cruzar(cromosoma1, cromosoma2)
        return cruce 
    
    def mutar(self, cromosoma, prob):
        #Devuelve el cromosoma mutado
        mutante = self.fun_mutar(cromosoma, prob)
        return mutante

    def fitness(self, cromosoma):
        #Función de valoración
        valoracion = self.fun_fitness(cromosoma)
        return valoracion


# Función interpreta lista de 0's y 1's como número natural:  

def binario_a_decimal(x):
    return sum(b * (2 ** i) for (i, b) in enumerate(x)) 


'''
Alternativas para el cruce   
       
'''
def alternativa_cruce1(cromosoma1,cromosoma2):
        len_cadena = len(cromosoma1)
        corte1 = random.randint(0, len_cadena - 1) 
        corte2 = random.randint(corte1 + 1, len_cadena) 
       
        for i in range(corte1, corte2):
            k = i
            cromosoma1[k] = cromosoma2[i]
            cromosoma2[i] = cromosoma1[k]
        return [cromosoma1, cromosoma2]

def alternativa_cruce2(cromosoma1,cromosoma2):
    l1 = len(cromosoma1)
    l2 = len(cromosoma2)
    cruce1 = cromosoma1[0:int(l1 / 3)] + cromosoma2[int(l2 / 3):-int(l2/3)] + cromosoma1[-int(l1 / 3):l1]
    cruce2 = cromosoma2[0:int(l2 / 3)] + cromosoma1[int(l1 / 3):-int(l1/3)] + cromosoma2[-int(l1 / 3):l2]
    return [cruce1, cruce2]

def alternativa_cruce3(cromosoma1,cromosoma2):
        len_cadena = len(cromosoma1)
        corte1 = random.randint(0, len_cadena - 1) # genera una posicion aleatoria
        corte2 = random.randint(corte1 + 1, len_cadena) 
       
        for i in range(corte1, corte2):
            k = random.randint(1, len(cromosoma2) - 1)
            cromosoma1[k] = cromosoma2[i]
            cromosoma2[i] = cromosoma1[k]
        return [cromosoma1, cromosoma2]



'''
Alternativas para la mutacion   
       
'''

def alternativa_mutar1(cromosoma, prob):

    if prob > random.uniform(0, 1):
        pos_mutar = random.randint(0, len(cromosoma)-1)
        if cromosoma[pos_mutar] == 1:
            cromosoma[pos_mutar] = 0
        else:
            cromosoma[pos_mutar] = 1
    return cromosoma     

def alternativa_mutar2(cromosoma, prob):
    
        for i in range(len(cromosoma)):
            if random.uniform(0, 1) > prob:
                k = random.randint(1, len(cromosoma) - 1)
                cromosoma[i], cromosoma[k] = cromosoma[k], cromosoma[i]
        return cromosoma

def alternativa_mutar3(cromosoma, prob):

    for _ in range(len(cromosoma)):
        if random.uniform(0, 1) > prob:
            punto = random.randint(1, len(cromosoma) - 1)
            nuevo_valor = random.randint(0,1)
            while nuevo_valor == cromosoma[punto]:
                nuevo_valor = random.randint(0,1)
            cromosoma[punto] = nuevo_valor
    return cromosoma



'''
Alternativas para la seleccion   
       
'''

def seleccion_aleatoria(problema_genetico, poblacion, n, k, opt):
    seleccionados = []
    i = 0
    for _ in range(n):
        escogidos = aleatorio(poblacion,k)
        seleccionado = opt(escogidos, key = problema_genetico.fitness)
        seleccionados.append(seleccionado)
        while(i != k):
            escogidos.pop()
            i += 1
    return seleccionados

def aleatorio(poblacion,k):
    participantes = []
    for _ in range(k):
        punto = random.randint(0, len(poblacion)-1)
        elegidos = poblacion[punto]
        participantes.append(elegidos)
    return participantes

def seleccion_por_torneo(problema_genetico, poblacion, n, k, opt):
    seleccionados = []
    for _ in range(n):
        participantes = random.sample(poblacion, k)
        seleccionado = opt(participantes, key = problema_genetico.fitness)
        seleccionados.append(seleccionado)
    return seleccionados

def seleccion_por_doble_torneo(problema_genetico, poblacion, n, k, opt):
    seleccionados = []
    participantes1 = []
    participantes2 = []
    clasificacion = []
    q = 0
    for _ in range(n):
        for _ in range (k):
            punto1 = random.randint(0, len(poblacion)-1)
            punto2 = random.randint(0, len(poblacion)-1)
            elegidos1 = poblacion[punto1]
            elegidos2 = poblacion[punto2]
            participantes1.append(elegidos1)
            participantes2.append(elegidos2)
        seleccionado1 = opt(participantes1, key = problema_genetico.fitness)
        seleccionado2 = opt(participantes2, key = problema_genetico.fitness)
        clasificacion.append(seleccionado1)
        clasificacion.append(seleccionado2)
        clasificacion.sort(reverse=True)
        seleccionados = clasificacion
        while (q != k):
            participantes1.pop()
            participantes2.pop()
            q += 1
    return seleccionados





def fun_fitness_cuad(cromosoma):
    # Función de valoración que eleva al cuadrado el número recibido en binario
    n = binario_a_decimal(cromosoma)**2
    return n

def deco_x(x):
    return [binario_a_decimal(x[:4]), binario_a_decimal(x[4:])] 

def poblacion_inicial(problema_genetico, size):
    l = []
    for i in range(size):
        l.append([random.choice(problema_genetico.genes) for i in range(problema_genetico.longitud_individuos)])                
    return l


def cruza_padres(problema_genetico, padres):
    l = []
    while padres != []:
        l.extend(problema_genetico.cruzar(padres[0], padres[1]))
        padres.pop(0)
        padres.pop(0)
    return l


def muta_individuos(problema_genetico, poblacion, prob):
    return [problema_genetico.mutar(x, prob) for x in poblacion]


def nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar, AS):
    if (AS == 1):
        padres2 = seleccion_aleatoria(problema_genetico, poblacion, n_directos, k, opt) 
        padres1 = seleccion_aleatoria(problema_genetico, poblacion, n_padres , k, opt)
    if (AS == 2):
        padres2 = seleccion_por_torneo(problema_genetico, poblacion, n_directos, k, opt) 
        padres1 = seleccion_por_torneo(problema_genetico, poblacion, n_padres , k, opt)
    if (AS == 3):
        padres2 = seleccion_por_doble_torneo(problema_genetico, poblacion, n_directos, k, opt) 
        padres1 = seleccion_por_doble_torneo(problema_genetico, poblacion, n_padres , k, opt)           
    cruces =  cruza_padres(problema_genetico,padres1)
    generacion = padres2 + cruces
    resultado_mutaciones = muta_individuos(problema_genetico, generacion, prob_mutar)
    return resultado_mutaciones


def algoritmo_genetico_t(problema_genetico, k, opt, ngen, size, prop_cruces, prob_mutar, AS):
    poblacion = poblacion_inicial(problema_genetico, size)
    print("Poblacion Inicial")
    print(poblacion)
    n_padres = round(size * prop_cruces)
    n_padres = int (n_padres if n_padres % 2 == 0 else n_padres - 1)
    n_directos = size - n_padres
    for _ in range(ngen):
        poblacion = nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar, AS)
        print("Nueva población")
        print(poblacion)
    mejor_cr = opt(poblacion, key = problema_genetico.fitness)
    mejor = problema_genetico.decodificar(mejor_cr)
    return (mejor, problema_genetico.fitness(mejor_cr)) 
 

def decodifica_mochila(cromosoma, n_objetos, pesos, capacidad):
    peso_en_mochila = 0
    l = []
    for i in range(n_objetos):
        if cromosoma[i] == 1 and peso_en_mochila + pesos[i] <= capacidad:
            l.append(1)
            peso_en_mochila += pesos[i]
        elif cromosoma[i] == 0 or peso_en_mochila + pesos[i] > capacidad:
            l.append(0)
    return l 

def fitness_mochila(cromosoma, n_objetos, pesos, capacidad, valores):
    objetos_en_mochila = decodifica_mochila(cromosoma, n_objetos, pesos, capacidad)
    valor = 0
    for i in range(n_objetos):
        if objetos_en_mochila[i] == 1:
            valor += valores[i]
    return valor
            

pesos1 = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
valores1 = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]

pesos2 = [70,73,77,80,82,87,90,94,98,106,110,113,115,118,120]
valores2 = [135,139,149,150,156,163,173,184,192,201,210,214,221,229,240]

pesos3 = [382745,799601,909247,729069,467902, 44328,
       34610,698150,823460,903959,853665,551830,610856,
       670702,488960,951111,323046,446298,931161, 31385,496951,264724,224916,169684]
valores3 = [825594,1677009,1676628,1523970, 943972,  97426,
       69666,1296457,1679693,1902996,
       1844992,1049289,1252836,1319836, 953277,2067538, 675367,
       853655,1826027, 65731, 901489, 577243, 466257, 369261]


def fitness_mochila_1(cromosoma):
    v = fitness_mochila(cromosoma, 10, pesos1, 165, valores1)
    return v

def decodifica_mochila_1(cromosoma):
    v = decodifica_mochila(cromosoma, 10, pesos1, 165)
    return v


def fitness_mochila_2(cromosoma):
    v = fitness_mochila(cromosoma, 15, pesos2, 750, valores2)
    return v

def decodifica_mochila_2(cromosoma):
    v = decodifica_mochila(cromosoma, 14, pesos2, 750)
    return v


def fitness_mochila_3(cromosoma):
    v = fitness_mochila(cromosoma, 24, pesos3, 6404180 , valores3)
    return v

def decodifica_mochila_3(cromosoma):
    v = decodifica_mochila(cromosoma, 24, pesos3, 6404180)
    return v

def Problema_Escoger(PP):
    PC = int(input(print("Escoja modo de cruce (1-3) ")))
    PM = int(input(print("Escoja modo de mutar (1-3) ")))
    if (PP == 1):
        m1g = Problema_Genetico([0,1], decodifica_mochila_1, Problema_Cruce(PC), Problema_Mutar(PM), fitness_mochila_1, 10)
        return m1g

    if (PP == 2):
        m2g = Problema_Genetico([0,1], decodifica_mochila_2, Problema_Cruce(PC), Problema_Mutar(PM), fitness_mochila_2, 15)
        return m2g

    if (PP == 3):
        m3g = Problema_Genetico([0,1], decodifica_mochila_3, Problema_Cruce(PC),  Problema_Mutar(PM), fitness_mochila_3,24)
        return m3g

def Problema_Cruce(PC):
    if (PC == 1):
        return alternativa_cruce1
    if (PC == 2):
        return alternativa_cruce2
    if (PC == 3):
        return alternativa_cruce3

def Problema_Mutar(PM):
    if (PM == 1):
        return alternativa_mutar1
    if (PM == 2):
        return alternativa_mutar2
    if (PM == 3):
        return alternativa_mutar3                 

if __name__ == "__main__":
    # Problema de la mochila 1:
    # 10 objetos, peso máximo 165
    # _______________________________________________________
    # Solución óptima= [1,1,1,1,0,1,0,0,0,0], con valor 309

    # Problema de la mochila 2:
    # 15 objetos, peso máximo 750
    # _______________________________________________________
    # Solución óptima= [1,0,1,0,1,0,1,1,1,0,0,0,0,1,1] con valor 1458

    # Problema de la mochila 3:
    # 24 objetos, peso máximo 6404180
    # _______________________________________________________
    # Solución óptima= [1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1] con valoración 13549094

    PP = int(input(print("Escoja el problema de la mochila (1-3) ")))
    AS = int(input(print("Escoja el metodo de seleccion (1-3) ")))
    print(algoritmo_genetico_t(Problema_Escoger(PP), 3, max, 100, 50, 0.8, 0.05, AS))
