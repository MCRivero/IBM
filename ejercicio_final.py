""" Enunciado 
Escribir un programa en Python que genere una matriz de tamaño NxN y la llene con números aleatorios entre 0 y 9. 
El programa deberá imprimir la matriz generada y luego calcular la suma de los elementos de cada fila y columna. 
Finalmente, deberá imprimir la suma de cada fila y columna.""" 

# 1. Generar una matriz cuadrada de tamaño NXN. N es un numero entero ingresado por el usuario
n_filas = 0
n_columnas = 0
lista=[]

n_tamaño_matriz = int(input("Introduzca el tamaño de la matriz: "))

print('Filas:', n_tamaño_matriz, 'columnas:', n_tamaño_matriz)
print(type(n_tamaño_matriz))

print('----------------------------')

# 2. Rellenar la matriz con numeros aleatorios entre 0 y 9.

while n_filas < n_tamaño_matriz:
    while n_columnas < n_tamaño_matriz:
        lista[n_filas,n_columnas] = 2
        print(lista[n_filas, n_columnas])
        n_columnas += 1
    n_filas += 1

# 3. Imprimir la matriz


# 4. Calcular la suma de cada fila y columna


# 5. Imprimir la suma de cada fila y columna
