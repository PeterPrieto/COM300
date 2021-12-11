import time
import platform
from os import system
from math import inf as infinity
from random import choice #servirá para escoger un elemento al azar de una lista 
import numpy as np #trabajo con matrices 

HUMANO = -1
COMPUTADOR = +1
n = 4
board = np.zeros((n, n)) #npzeros regresa un array/matriz de puro ceros

def HUMANO_turn(c_choice, h_choice):
    """
    The HUMANO plays choosing a valid move.
    :param c_choice: COMPUTADORuter's choice X or O
    :param h_choice: HUMANO's choice X or O
    :return:
    """
    depth = len(empty_cells(board)) #analiza si todavia se pueden hacer jugadas
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1

    moves = {} #coordenadas disponibles 
    k = 1
    for i in range(n): 
        for j in range(n):
            moves[k] = [i, j]  #mapeo de movimientos validos
            k += 1 

    clean()
    print(f"turno HUMANO [{h_choice}]")
    render(board, c_choice, h_choice)

    while move < 1 or move > k - 1: #valida los movimientos
        try:
            move = int(input(f"Use numpad (1..{k-1}): "))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMANO)

            if not can_move:
                print("Bad move")
                move = -1
        except (EOFError, KeyboardInterrupt):
            print("Bye")
            exit()
        except (KeyError, ValueError):
            print("Bad choice")

def evaluate(estado):
    """
    Evaluacion Heuristica
    
    """
    if wins(estado, COMPUTADOR):
        score = +1
    elif wins(estado, HUMANO):
        score = -1
    else:
        score = 0

    return score  #funcion de evaluacion que devolvera el valor de estado de la partida cuando se llegue a la hoja

def wins(estado, player): #sirve para buscar condiciones de victoria y regresa un valor booleano
    """
    Verifica si un jugador en especifico gana y como gana. Retorna un booleano
    """
    win_state = [
        [estado[0][0], estado[1][1], estado[2][2]], #analiza las diagonales izq a der
        [estado[2][0], estado[1][1], estado[0][2]], #analiza las diagonales de der a izq
    ]

    win_state.extend([[estado[i][j] for j in range(3)] for i in range(3)]) # comprueba las verticales de 3 en 3
    win_state.extend([[estado[i][j] for i in range(3)] for j in range(3)]) # comprueba las horizontales de 3 en 3

    if [player, player, player] in win_state: #verifica la victoria para el jugador humano y retorna True si ganó la partida
        return True
    else:
        return False 
def game_over(estado):
    """
    Llama a wins para pedir el booleano y saber cual de los dos ganó
    """
    return wins(estado, HUMANO) or wins(estado, COMPUTADOR) 


def empty_cells(estado):
    """
    Cada celda vacía se agregará a la lista de celdas
    :parametro estado, estado de tablero actual
    :devuelve, una lista de las celdas vacias
    """
    cells = []

    for x, fila in enumerate(estado): #muestreo de todas las filas y columnas para encontrar y agregar celdas vacias
        for y, cell in enumerate(fila):
            if cell == 0:
                cells.append([x, y])
    return cells


def valid_move(x, y):
    """
    Si las coordenadas x,y corresponden a un 0 en la lista de empty cells es un movimiento valido
    """
    if [x, y] in empty_cells(board): # devuelve true si la coordenada que se le manda es la de una celda vacia
        return True
    else:
        return False

def set_move(x, y, player):
    """
   si valid move dice que es un movimiento valido, te puedes mover a esa coordenada
    """
    if valid_move(x, y):
        board[x][y] = player #en base a lo que retorne la funcion anterior se hará o no el movimiento
        return True
    else:
        return False

def minimax(estado, depth, player):
    """
    Funcion IA que elige la mejor movida
    AI function that choice the best move
    :parametro estado, estado actual en el tablero
    :param depth, indice del nodo en el arbol (0 <= depth <= 9), pero nunca nueve.
    :param player, un HUMANOo o un COMPUTADORutador
    :devuelve, una lista con [la mejor fila, la mejor columna, el mejor score]
    """
    if player == COMPUTADOR:
        best = [-1, -1, -infinity] # Agente Maximizante
    else:
        best = [-1, -1, +infinity] # Agente Minimizante

    if depth == 0 or game_over(estado): #cuando se haya llegado a la hoja o a un game over se llama a la funcion de eval.
        score = evaluate(estado)        #se retorna la evaluacion de utilidad
        return [-1, -1, score]          # si no se cumple esta condicion el juego sigue 

    for x, y in empty_cells(estado): #revisa cada accion posible en cada movimiento 
        estado[x][y] = player 

        score = minimax(estado, depth - 1, -player) # llama recursivamente a minimax para calcular los nodos intermedios
                                                    # evalua cada uno de los hijos
                                                    # -player porque es turno del otro jugador

        estado[x][y] = 0
        score[0], score[1] = x, y

        if player == COMPUTADOR:
            if score[2] > best[2]: #toma el valor maximo si Max esta jugando
                best = score  
        else:
            if score[2] < best[2]: #toma el minimo si Min esta jugando
                best = score  

    return best
def clean():
    """
    Limpia la consola
    """
    os_name = platform.system().lower()
    if "windows" in os_name:
        system("cls")
    else:
        system("clear")

def render(estado, c_choice, h_choice):
    """
    Crea el tablero donde se jugara
    :param estado: current estado of the board
    """

    box = 1
    chars = {-1: h_choice, +1: c_choice, 0: " "}
    str_line = "-" * 20
    print("\n" + str_line)
    for fila in estado:
        for cell in fila:
            symbol = chars[cell]
            print(f"| {symbol if symbol != ' ' else ' ' } |", end="")
            box += 1
        print("\n" + str_line)

def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: COMPUTADORuter's choice X or O
    :param h_choice: HUMANO's choice X or O
    :return:
    """
    best = [-1, -1, -infinity]  
    x, y = -1, -1

    for i in range(n - 2):
        for j in range(n - 2):
            estado = board[j : j + 3, i : i + 3] #ira verificando el estado del tablero en porciones de 3x3

            depth = len(empty_cells(estado)) #verifica si todavia quedan jugadas disponibles
            if game_over(estado): #comprueba si el juego terminó
                return True

            clean()
            print(f"Juega COMPUTADORA [{c_choice}]")
            render(board, c_choice, h_choice)

            if depth == 9: #elige la primera jugada
                x = choice([0, 1, 2])
                y = choice([0, 1, 2])
            else:
                score = minimax(estado, depth, COMPUTADOR) #si el humano empezó llama a minimax
                print(score)
                if score[2] > best[2]:
                    best = score  # max value
                    x, y = best[0] + j, best[1] + i
                    print(x, y, best)
                    time.sleep(2)
    print(x, y)
    set_move(x, y, COMPUTADOR)
    # return game_over
    time.sleep(2)

def HUMANO_turn(c_choice, h_choice):
    """
    The HUMANO plays choosing a valid move.
    :param c_choice: COMPUTADORuter's choice X or O
    :param h_choice: HUMANO's choice X or O
    :return:
    """
    depth = len(empty_cells(board)) #analiza si todavia se pueden hacer jugadas
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1

    moves = {} #coordenadas disponibles 
    k = 1
    for i in range(n): 
        for j in range(n):
            moves[k] = [i, j]  #mapeo de movimientos validos
            k += 1 

    clean()
    print(f"turno HUMANO [{h_choice}]")
    render(board, c_choice, h_choice)

    while move < 1 or move > k - 1: #valida los movimientos
        try:
            move = int(input(f"Use numpad (1..{k-1}): "))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMANO)

            if not can_move:
                print("Movimiento Erroneo")
                move = -1
        except (EOFError, KeyboardInterrupt):
            print("Bye")
            exit()
        except (KeyError, ValueError):
            print("Mala respuesta")


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ""  # X or O
    c_choice = ""  # X or O
    first = ""  # if HUMANO is the first

    # HUMANO chooses X or O to play
    while h_choice != "O" and h_choice != "X":
        try:
            print("")
            h_choice = input("Elige X o O\nElegido: ").upper()
        except (EOFError, KeyboardInterrupt):
            print("Bye")
            exit()
        except (KeyError, ValueError):
            print("Mala Respuesta")

    # Setting COMPUTADORuter's choice
    if h_choice == "X":
        c_choice = "O"
    else:
        c_choice = "X"

    # HUMANO may starts first
    clean()
    while first != "Y" and first != "N":
        try:
            first = input("Empezar primero?[y/n]: ").upper()
        except (EOFError, KeyboardInterrupt):
            print("Bye")
            exit()
        except (KeyError, ValueError):
            print("Mala Respuesta")

    # Main loop of this game
    game_over = False
    while len(empty_cells(board)) > 0 and not game_over:
        if first == "N":
            game_over = ai_turn(c_choice, h_choice)
            first = ""

        HUMANO_turn(c_choice, h_choice)
        game_over = ai_turn(c_choice, h_choice)

    # Mensaje de Game Over
    for i in range(n - 2):
        for j in range(n - 2):
            estado = board[j : j + 3, i : i + 3]

            if wins(estado, HUMANO):
                clean()
                render(board, c_choice, h_choice)
                print("GANASTE")
                exit()

            elif wins(estado, COMPUTADOR):
                clean()
                render(board, c_choice, h_choice)
                print("PERDISTE")
                exit()

    clean()
    render(board, c_choice, h_choice)
    #print("Empate!")

    exit()


if __name__ == "__main__":
    main()