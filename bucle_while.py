# Un bucle while, repite un trozo de codigo iterativamente 
# mientras se cumpla una determinada condicion
a = 0
while a < 3:
    print(a, end=' ')   #Acabamos con espacios en lugar de salto de linea
    a += 1              #Equivalente a: a = a + 1
print(a)                #Estamos fuera del while
print('Hemos salido fuera del while')

# Al comenzar cada iteración la expresión de inicio del while es evaluada. Si la expresión se cumple 
# (devuelve True), se vuelve a entrar en el while. Si no se cumple (devuelve False), el while deja de 
# ejecutarse y pasamos a la siguiente sentencia tras el while.

# Bucles y las sentencias continue, break, pass y los bloques else

# break: Interrumpe el flujo y sale fuera de bucle.
# continue: Salta al comienzo de la siguiente iteración del bucle
# pass: No hace nada. Es una sentencia vacía.
# Else: Al finalizar un bucle: Se ejecuta sólo si el bucle ha finalizado con normalidad. 
#       Es decir, se ejecuta si el bucle finaliza sin haber ejecutado un break.

# Sentencia break
a=5
while a:                #Utilizamos la propia variable como condicion
    print(a, end='  ')
    #a == 2
    if a == 2:
        break
    a -= 1              #Equivalente a: a = a - 1
print('\nFuera del bucle')
print('Valor de "a": {}'.format(a))

print ('-----------------------------')

# Sentencia continue
a = 7
while bool(a):
    #a -= 1             #Equivalente a: a = a - 1
    a = a - 1
    if a % 2 == 0:
        continue
    print(a, end=' ')
print('\nFuera del bucle')