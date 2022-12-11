def movimiento_valido_caballo(inicio:tuple, fin:tuple):
    dif_x = abs(inicio[0] - fin[0])
    dif_y = abs(inicio[1] - fin[1])
    if dif_x + dif_y == 3 and dif_y > 0 and dif_x > 0:
        return True
    return False

def todos_los_movimientos_validos(tablero:dict, inicio:int):
    movimientos = [] #lista de tuplas inicio-fin
    for mov in tablero:
        if movimiento_valido_caballo(tablero[inicio],tablero[mov]):
            movimientos.append((inicio, mov))
    return movimientos

tablero = {1:(0,0), 2:(0,1), 3:(0,2),4:(1,0), 5:(1,1), 6:(1,2),
           7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}

total = []
for i in range(10):
    lista = todos_los_movimientos_validos(tablero, i)
    total.extend(lista)


print(total)
print(len(total))
 

