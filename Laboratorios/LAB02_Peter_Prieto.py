vector = ['C','D','A','E','B']
cont = 0
reinicio = True
print("Primer Metodo")
print(vector)
# 1.Solo se puede intercambiar letras vecinas #
# Ordena para A #
while reinicio:
    reinicio = False
    cont = 0
    for num in vector:
        if vector[0] != 'A':
            if num == "A":
                aux = num
                aux2 = vector[cont-1]
                vector[cont-1] = aux
                vector[cont] = aux2
                reinicio = True
                print(vector)
                break
        cont += 1
# Ordena para B #
cont = 0
reinicio = True
while reinicio:
    reinicio = False
    cont = 0
    for num in vector:
        if vector[1] != 'B':
            if num == "B":
                aux = num
                aux2 = vector[cont-1]
                vector[cont-1] = aux
                vector[cont] = aux2
                reinicio = True
                print(vector)
                break
        cont += 1
# Ordena para C #
cont = 0
reinicio = True
while reinicio:
    reinicio = False
    cont = 0
    for num in vector:
        if vector[2] != 'C':
            if num == "C":
                aux = num
                aux2 = vector[cont-1]
                vector[cont-1] = aux
                vector[cont] = aux2
                reinicio = True
                print(vector)
                break
        cont += 1
# Ordena para D #
cont = 0
reinicio = True
while reinicio:
    reinicio = False
    cont = 0
    for num in vector:
        if vector[3] != 'D':
            if num == "D":
                aux = num
                aux2 = vector[cont-1]
                vector[cont-1] = aux
                vector[cont] = aux2
                reinicio = True
                print(vector)
                break
        cont += 1
# Ordena para E #
cont = 0
reinicio = True
while reinicio:
    reinicio = False
    cont = 0
    for num in vector:
        if vector[4] != 'E':
            if num == "E":
                aux = num
                aux2 = vector[cont-1]
                vector[cont-1] = aux
                vector[cont] = aux2
                reinicio = True
                print(vector)
                break
        cont += 1




# 2.Solo se puede realizar un intercambio a la vez. #
vector2 = ['C','D','A','E','B']
print("Segundo Metodo")
print(vector2)
cont = 0
reinicio = True
while reinicio:
    reinicio = False
    cont = 0
    for num in vector2:
        if vector2[0] != 'A':
            if num == "A":
                aux = num
                aux2 = vector2[0]
                vector2[0] = aux
                vector2[cont] = aux2
                reinicio = True
                print(vector2)
                break
        cont += 1
cont = 0
reinicio = True
while reinicio:
    reinicio = False
    cont = 0
    for num in vector2:
        if vector2[1] != 'B':
            if num == "B":
                aux = num
                aux2 = vector2[1]
                vector2[1] = aux
                vector2[cont] = aux2
                reinicio = True
                print(vector2)
                break
        cont += 1 
cont = 0
reinicio = True
while reinicio:
    reinicio = False
    cont = 0
    for num in vector2:
        if vector2[2] != 'C':
            if num == "C":
                aux = num
                aux2 = vector2[2]
                vector2[2] = aux
                vector2[cont] = aux2
                reinicio = True
                print(vector2)
                break
        cont += 1
cont = 0
reinicio = True
while reinicio:
    reinicio = False
    cont = 0
    for num in vector2:
        if vector2[3] != 'D':
            if num == "D":
                aux = num
                aux2 = vector2[3]
                vector2[3] = aux
                vector2[cont] = aux2
                reinicio = True
                print(vector2)
                break
        cont += 1
cont = 0
reinicio = True
while reinicio:
    reinicio = False
    cont = 0
    for num in vector2:
        if vector2[4] != 'E':
            if num == "E":
                aux = num
                aux2 = vector2[4]
                vector2[4] = aux
                vector2[cont] = aux2
                reinicio = True
                print(vector2)
                break
        cont += 1        