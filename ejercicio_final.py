""" Enunciado 
Escribir un programa en Python que genere una matriz de tamaño NxN y la llene con números aleatorios entre 0 y 9. 
El programa deberá imprimir la matriz generada y luego calcular la suma de los elementos de cada fila y columna. 
Finalmente, deberá imprimir la suma de cada fila y columna.""" 

import random

# 1. Generar una matriz cuadrada de tamaño NXN. N es un numero entero ingresado por el usuario
matriz=[]

N = int(input("Introduzca el tamaño de la matriz: "))


# 2. Rellenar la matriz con numeros aleatorios entre 0 y 9.

for i in range(N):
    fila = []
    for j in range(N):
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