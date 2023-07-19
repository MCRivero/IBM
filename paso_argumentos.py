#Por defecto los argumentos se pasan por posicion (PAGINA 12)
#PYTHON nos permite pasarles argumentos a las funciones de distintas maneras
#POR POSICION (por defecto)
def f(a,b,c):
    print('POR POSICION: ', a,b,c)

f(1,2,3)

print('---------------------')

#POR KEYWORDS. Sintaxis nombre=valor
def f(a,b,c):
    print('POR SINTAXIS NOMBRE-VALOR: ', a,b,c)

f(c=12,a=10,b=100)

print('---------------------')

#VALORES POR DEFECTO EN LA LLAMADA DE LA FUNCION
def f(a,b=10,c=30):
    print('VALORES POR DEFECTO EN LA LLAMADA DE LA FUNCION: ', a,b,c)

f(1)
f(1,12)
f(1,12,19)

print('---------------------')

#EN LA DEFINICION DE LA FUNCION SE INDICA QUE SE LE PASARA UN NUMERO ARBITRARIO DE ARGUMENTOS
#COLECCION DE ARGUMENTOS
def f(*args):   # Acepta numero erbitrario de argumentos
    print(args)

f()             # Si no hay argumemtos el resultado es una tupla vacia
f(1)
f(1,2)
f(1,2,3,4,5,6)

print('---------------------')

#CON DOBLE ** PASAREMOS LOS ARGUMENTOS POR NOMBRE 
def f(**args):
    print(args)

f()             # Si no hay argumentos, args es un diccionario vacio
f(a=1)          # El resultado será {'a': 1}
f(a=1,b=2)      # El resultado será {'a': 1, 'b': 2}
f(a=1,c=3,b=2)  # El resultado será {'a': 1, 'c': 3, 'b': 2}

print('---------------------')

# DESEMPAQUETANDO UNA COLECCION DE ARGUMENTOS POSICIONALES O POR KEYWORD
# SE PUEDE DESEMPAQUETAR UN DICCIONARIO UTILIZANDO LA SINTAXIS **
def f(a, b, c, d):
    print('DESEMPAQUETANDO: ', a,b,c,d)

argumentos = {'b':20, 'a':1, 'c':300, 'd':4000}

f(**argumentos) #desempaquetamos el diccionario argumentos con **

argumentos = {'b':200, 'c':300, 'd':400}

f(10, **argumentos) #Podemos combinar argumentos posicionales con dict

print('---------------------')

#ARGUMENTOS QUE SOLO PUEDEN SER PASADOS POR CLAVE
def f(a,*,b,c):     #Define 'b' y 'c' como keyword-only con el *
    print(a,b,c)

f(1,b=10,c=100)     # RESULTADO = 1 10 100. La plaza del * queda vacia

#f(1, 10,100)        #Este ejemplo da error al no pasar argumentos keyword-only
                    # RESULTADO = TypeError: f() takes 1 positional argument but 3 were given

def f(a,*b,c):      #Hay que pasar 'c' por clave obligatoriamente
    print(a,b,c)

f(1, c=2)           # RESULTADO = 1 () 2

f(1,2,c=3)          # RESULTADO = 1 (2,) 3

f(1,2,3,4,5,c=10)   # RESULTADO = 1 (2, 3, 4, 5) 10

# LOS ARGUMENTOS TRAS EL * SE CONVIERTEN EN KEYWORD-ONLY
# VER EJEMPLO DE SU USO EN PAGINA 14 Y 15 (ZIP Y PRINT)