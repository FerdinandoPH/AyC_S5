import random

def ej3_cambio_billetes(cantidad :int, valBill :list, cantBill :list) -> list:
    """ Devuelve la cantidad de billetes necesarios para devolver una cantidad de dinero con la menor cantidad de billetes posibles con un numero limitado de billetes de cada tipo
    
    >>> ej3_cambio_billetes(10, [1, 5, 10], [2, 2, 2])
    [0, 0, 1]

    >>> ej3_cambio_billetes(10, [1, 5, 10], [2, 2, 0])
    [0, 2, 0]

    >>> ej3_cambio_billetes(2, [5, 10, 20], [5, 5, 5])
    [inf, inf, inf]

    >>> ej3_cambio_billetes(34, [1, 3, 7, 11], [5, 3, 1, 2])
    [2, 1, 1, 2]

    >>> ej3_cambio_billetes(2, [1, 5, 10], [2, 2, 2])
    [2, 0, 0]

    >>> ej3_cambio_billetes(50, [1, 5, 10], [2, 2, 2])
    [inf, inf, inf]
    """
    matriz = []                                                                                     # O(1)
    for i in range(len(valBill)):                                                                   # O(nm^2)
        matriz.append([])                                                                           # O(1)
        for j in range(cantidad+1):                                                                 # O(nm)
            if j == 0:                                                                              # O(m)
                matriz[i].append([])                                                                # O(1)
                for k in range(len(valBill)):                                                       # O(m)
                    matriz[i][j].append(0)                                                          # O(1)
            else:
                matriz[i].append([])                                                                # O(1)
                for k in range(len(valBill)):                                                       # O(m)
                    matriz[i][j].append(float("inf"))                                               # O(1)
    

    for iMaxVal in range(len(valBill)):                                                             # O(nm^2)
        for cant in range(1, cantidad+1):                                                           # O(nm)
            if iMaxVal == 0 and cant < valBill[iMaxVal]:                                            # O(m)
                pass

            elif iMaxVal == 0:
                rellenar = cant // valBill[0]                                                       # O(1)
                if rellenar <= cantBill[0] and valBill[0]*rellenar == cant:                         # O(m)
                    matriz[0][cant][0] = rellenar                                                   # O(1)
                
                    for i in range(1, len(valBill)):                                                # O(m)
                        matriz[iMaxVal][cant][i] = 0                                                # O(1)
                
            elif cant < valBill[iMaxVal]:
                matriz[iMaxVal][cant] = matriz[iMaxVal-1][cant]                                     # O(1)

            else:
                temp = cant // valBill[iMaxVal]                                                     # O(1)
                if temp > cantBill[iMaxVal]:                                                        # O(1)
                    temp = cantBill[iMaxVal]                                                        # O(1)

                for i in range(len(valBill)):                                                       # O(m)
                    matriz[iMaxVal][cant][i] = matriz[iMaxVal-1][cant-(temp*valBill[iMaxVal])][i]   # O(1)
                if float("inf") not in matriz[iMaxVal][cant]:                                       # O(1)
                    matriz[iMaxVal][cant][iMaxVal] = temp                                           # O(1)
    
    return matriz[len(valBill)-1][cantidad]                                                         # O(1)
# O(nm^2) siendo n la cantidad y m el tamaño de la lista de billetes


def ej6_quidditch(apostado :float, calidades :list) -> float:
    """ Devuelve la cantidad de dinero ganada en una apuesta de quidditch dada la apuesta inicial y la calidad de los equipos sabiendo que un equipo tiene que ganar seis partidos en total para ganar el torneo

    >>> ej6_quidditch(1, [1, 2, 3, 4])
    208.875377339135

    >>> ej6_quidditch(100, [1, 1, 1, 1])
    400.0

    >>> ej6_quiditch(50, [10, 5, 20, 5])
    420.42058795339176

    >>> ej6_quidditch(10, [97, 1, 1, 1])
    10.000000014973988
    """
    matriz = []                                                                             # O(1)
    sumaCalidades = calidades[0] + calidades[1] + calidades[2] + calidades[3]               # O(1)
    probabilidades = [calidades[0]/sumaCalidades, calidades[1]/sumaCalidades, calidades[2]/sumaCalidades, calidades[3]/sumaCalidades] # O(1)
    for x in range(7):                                                                      # O(1)
        matriz.append([])                                                                   # O(1)
        for y in range(7):                                                                  # O(1)
            matriz[x].append([])                                                            # O(1)
            for z in range(7):                                                              # O(1)
                matriz[x][y].append([])                                                     # O(1)
                for w in range(7):                                                          # O(1)
                    matriz[x][y][z].append([])                                              # O(1)
                    if [x,y,z,w] == [0,0,0,0]:                                              # O(1)
                        matriz[0][0][0][0] = 1                                              # O(1)
                    else:
                        matriz[x][y][z][w] = 0                                              # O(1)
                        if w-1 >= 0 and z<6 and y<6 and x<6:                                # O(1)
                            matriz[x][y][z][w] += probabilidades[0] * matriz[x][y][z][w-1]  # O(1)
                        if z-1 >= 0 and w<6 and y<6 and x<6:                                # O(1)
                            matriz[x][y][z][w] += probabilidades[1] * matriz[x][y][z-1][w]  # O(1)
                        if y-1 >= 0 and w<6 and z<6 and x<6:                                # O(1)
                            matriz[x][y][z][w] += probabilidades[2] * matriz[x][y-1][z][w]  # O(1)
                        if x-1 >= 0 and w<6 and z<6 and y<6:                                # O(1)
                            matriz[x][y][z][w] += probabilidades[3] * matriz[x-1][y][z][w]  # O(1)

    res = 0                                                                                 # O(1)
    for x in range(6):                                                                      # O(1)
        for y in range(6):                                                                  # O(1)
            for z in range(6):                                                              # O(1)
                res += matriz[x][y][z][6]                                                   # O(1)
    
    return apostado / res                                                                   # O(1)
# O(1)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
