""" Enunciado 
Escribir un programa en Python que genere una matriz de tamaño NxN y la llene con números aleatorios entre 0 y 9. 
El programa deberá imprimir la matriz generada y luego calcular la suma de los elementos de cada fila y columna. 
Finalmente, deberá imprimir la suma de cada fila y columna.""" 

import random

# 1. Generar una matriz cuadrada de tamaño NXN. N es un numero entero ingresado por el usuario
matriz=[]

def tamaño_matriz():
    NXN = int(input('Introduzca el tamaño de la matriz: '))
    return NXN    

matriz_valida = True
while matriz_valida:
    try:
        t_matriz = tamaño_matriz()
    except:
        ValueError: print('Solo admite valores numericos')
        break
    if t_matriz == 0:
        print('Indique tamaño de matriz')
        break
    elif t_matriz == 1:
        print('Matriz debe tener 2 dimensiones')
        break
    elif t_matriz > 10:
        print('Matriz debe ser menor o igual a 10')    
        break
    elif t_matriz < 0:
        print('Tamaño valido entre 1 y 10') 
        break

# 2. Rellenar la matriz con numeros aleatorios entre 0 y 9.

    for i in range(t_matriz):
        fila = []
        for j in range(t_matriz):
            fila.append(random.randint(0,9))
        matriz.append(fila)

# 3. Imprimir la matriz
    for fila in matriz:
        print(fila)

# 4. Calcular la suma de cada fila y columna
    suma_filas = []
    suma_columnas = [0] * len(matriz)

    for fila in matriz:
        suma_fila = sum(fila)
        suma_filas.append(suma_fila)
        for j, elemento in enumerate(fila):
            suma_columnas[j] += elemento    

# 5. Imprimir la suma de cada fila y columna
    print('suma filas:', suma_filas)
    print('suma_columnas:', suma_columnas)
    matriz_valida = False