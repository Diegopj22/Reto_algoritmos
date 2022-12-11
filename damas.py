"""
 El problema de las nreinas es colocar N reinas en un N*N tablero de ajedrez tal que ninguna reina pueda
 atacar a otras reinas colocadas en ese tablero de ajedrez.
 Esto significa que una reina no puede tener ninguna otra reina en su horizontal,vertical
 y diagonal.
"""
from __future__ import annotations

solution = []


def is_safe(board: list[list[int]], row: int, column: int) -> bool:
    """
    Esta función devuelve un valor booleano True si es seguro colocar una reina ahí 
    teniendo en cuenta el estado actual del tablero.
    Parametros :
    tablero(2D matrix) : board
    fila ,columna : coordenadas de la celda en el tablero
    Devuelve :
    Boolean Value
    """
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    for i in range(len(board)):
        if board[i][column] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] == 1:
            return False
    return True


def solve(board: list[list[int]], row: int) -> bool:
    """
    Crea un árbol de espacio de estado y llama a la función segura hasta que recibe un falso
    Booleano y termina esa rama y retrocede a la siguiente posible rama de solución.
    """
    if row >= len(board):
        """
        Si el númerro de fila excede N, tenemos un tablero con una combinación exitosa y 
        esa combinación se adjunta a la lista de soluciones y se imprime el tablero.
        """
        solution.append(board)
        printboard(board)
        print()
        return True
    for i in range(len(board)):
        """
        Para cada fila itera a través de cada columna para verificar si es factible colocar una reina allí.
        si todas las combinaciones para esa rama en particular tienen éxito,el tablero se reinicializará para la 
        siguiente combinación posible.
        """
        if is_safe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    return False


def printboard(board: list[list[int]]) -> None:
    """
    Imprime los tableros que tienen una combinación exitosa.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n=int(input("Introduce el número de reinas:"))
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("El total de soluciones son :", len(solution))