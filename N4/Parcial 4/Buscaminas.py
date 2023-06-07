
matriz= [[0, 0, 1, 1, 1, 0, 0, 1, 0 ],
        [0, 0, 1, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 1, 0, 0, 1, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0 ],
        [1, 1, 0, 0, 1, 0, 0, 1, 0 ],
        [0, 0, 0, 0, 0, 1, 0, 0, 0 ],
        [0, 1, 0, 1, 0, 0, 0, 0, 0 ],
        [0, 0, 1, 0, 0, 1, 0, 1, 0 ]]

def fila_con_num_minas(matriz:list, num_minas:int) -> int:

    minas_en_fila = 0
    for i in range(len(matriz)):

        for j in range(len(matriz[0])):
            valor = matriz[i][j]

            if valor == 1:
                minas_en_fila += 1

        if minas_en_fila >= num_minas:

            return i
        
def contar_minas_region(matriz:list, fila:int, columna:int) -> int:

    minas = 0
    for i in range(fila, fila+3):

        for j in range(columna, columna+3):

            if i >= 0 and i < len(matriz) and j >= 0 and j < len(matriz[0]):

                if matriz[i][j] == 1:
                    minas += 1

    return minas


