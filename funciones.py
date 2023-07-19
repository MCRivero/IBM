
def sumar(a,b):
    print(a,b)
    return a+b
    

x = sumar (7,3)
print(x)

def en_pantalla(frase1, frase2):
    print(frase1,frase2)

en_pantalla('Me gusta', ' Python')

# POLIMORFISMO - EN PYTHON LAS FUNCIONES NO TIENEN TIPO
# USAMOS LA FUNCION SUMAR CON NUMEROS Y STRINGS Y EN AMBOS CAOSOS ES VÁLIDA
sumar('Me gusta', ' Python')
# FIN POLIMORFISMO

# FUNCIONES ANIDADAS - ES POSIBLE CREAR FUNCIONES DENTRO DE FUNCIONES
def f1(a): # Funcion que encierra a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Funcion anidada, llamamos a f2 desde f1
        print(x)
    f2(b)
f1('FUNCION ANIDADA')
## FUNCIONES ANIDADAS

# RECURSIVIDAD - UNA FUNCION QUE SE LLAMA A SI MISMA
# LA FUNCION DEBE TENER UNA CONDICION DE SALIDA
def factorial(x):
    if x>1:
        print(x)
        return x*factorial(x-1)
    else:
        print('Factorial = 1')
        return 1
f=factorial(5)
print('Resultado de factorial')
print(f)
## FIN RECURSIVIDAD

# DEVOLVIENDO MULTIPLES VALORES
def maxim(lista):
    return max(lista), min(lista)

l = [1, 3, 5, 6, 0]

maximo, minimo = maxim(l)

print(maximo, minimo, sep= ' ')
## FIN DEVOLVIENDO MULTIPLES VALORES