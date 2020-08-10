direcciones = {
    'R': {
        'siguiente': 'D', #Siguiente dirección, cuando gira a la derecha
        'incremento': { #Incremento a las coordenadas en X y Y
            'x': 1, 
            'y': 0
        },
        'valida_movimiento': lambda x, y, n, m:  x < m # Función que valida si el movimiento es correcto deacuerdo a la dirección actual 
    },
    'D': {
        'siguiente': 'L',
        'incremento': {
            'x': 0,
            'y': 1
        },
        'valida_movimiento': lambda x, y, n, m:  y < n
    },
    'L': {
        'siguiente': 'U',
        'incremento': {
            'x': -1,
            'y': 0
        },
        'valida_movimiento': lambda x, y, n, m:  x > -1
    },
    'U': {
        'siguiente': 'R',
        'incremento': {
            'x': 0,
            'y': -1
        },
        'valida_movimiento': lambda x, y, n, m:  y > -1
    },
}

def ubicacionDisponible(posicion_y, posicion_x, ubicaciones_visitadas):
    ubicacion_disponible = len([item for item in ubicaciones_visitadas if item['x']
                             == posicion_x and item['y'] == posicion_y]) > 0

    return not ubicacion_disponible

def recorrerPosiciones(n, m):
    direccion = 'R'
    siguiente_direccion = 'R' #Direccion auxiliar
    posicion_x = 0
    posicion_y = 0
    siguiente_posicion_x = 0 #Posicion auxiliar en X 
    siguiente_posicion_y = 0 #Posicion auxiliar en Y
    posicion_disponible = True
    #Almacena una lista con las Posiciones visitadas
    posiciones_visitadas = [
        {
            'y': 0,
            'x': 0,
        }
    ]
    #Recorre las posiciones mientras exista una posición disponible
    while posicion_disponible:
        #Establece la Posiciones auxiliar con las Posiciones actuales
        siguiente_posicion_x = posicion_x
        siguiente_posicion_y = posicion_y
        #Incrementa las coordenas en función a la dirección actual
        siguiente_posicion_x += direcciones[siguiente_direccion]["incremento"]["x"]
        siguiente_posicion_y += direcciones[siguiente_direccion]["incremento"]["y"]
        #Valida si el siguiente movimiento esta dentro de los limites del Grid y si la ubicación esta disponible
        if (direcciones[siguiente_direccion]['valida_movimiento'](
                siguiente_posicion_x, siguiente_posicion_y, n, m) and ubicacionDisponible(siguiente_posicion_y, siguiente_posicion_x, posiciones_visitadas)):
            #Estable las Posiciones actuales con las Posiciones auxiliares
            posicion_y = siguiente_posicion_y
            posicion_x = siguiente_posicion_x
            # Agrega la posicion actual a la lista de Posiciones visitadas
            posiciones_visitadas.append({'y': posicion_y, 'x': posicion_x, })
            #Establece la dirección actual con la dirección auxiliar
            direccion = siguiente_direccion
        else:
            #Establece la siguiente direccion en función a la dirección actual 
            siguiente_direccion = direcciones[siguiente_direccion]["siguiente"]
            #Valida si aún existe una posición disponible. 
            #Termina cuando la siguiente dirección es igual a la dirección actual, ya que dio un giro completo sin encontrar una disponible
            posicion_disponible = (not siguiente_direccion == direccion)

    print(direccion)
    return direccion


print('(1, 1): R - ', recorrerPosiciones(1, 1))
print('(2, 2): L - ', recorrerPosiciones(2, 2))
print('(3, 1): D - ', recorrerPosiciones(3, 1))
print('(3, 3): R - ', recorrerPosiciones(3, 3))


