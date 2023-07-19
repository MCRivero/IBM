# If, elif, else
a = 10
b = 10
if a > b:
    print('a es mayor que b')
elif a == b:
    print('a es igual a b')
else:
    print('a es menor que b')
print('Ya salimos del condicional')

# Operador ternario
c = 10
d = 3
20 if c > d else 30

#Ejemplo 1
notaIn=int(input('Introduzca nota:'))

if notaIn < 5:
    calificacion = 'Suspenso'
else: calificacion = 'Aprobado'
print(calificacion)

#Ejemplo 2
edad=int(input('Introduzca edad:'))

if edad < 18:
    print('No puedes pasar')
elif edad > 100: print('Edad erronea')
else: print('Adelante')

#Ejemplo 3
nota=int(input("Introduce tu nota: "))
if nota<5:
    print("Suspenso")
elif nota<7:
    print("Aprobado")
elif nota<9:
    print("Notable")
else:
    print("Sobresaliente")
