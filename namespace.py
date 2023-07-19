# Un namespace es un lugar donde residen un conjunto de nombres.
# El namespace en el que reside un nombre define su ambito (SCOPE)
# Los nombres asignados dentro del ambito de una funcion, son sólo visibles por el codigo que reside dentro de esa misma funcion
# Un nombre declarado dentro de una funcion no puede ser referenciado desde fuera de esta.
# El ambito de una variable depende del lugar donde se asigno
# 1. es asignada en el interior de una funcion, es local a esa funcion
# 2. es asignada dentro de una funcion, sera nonlocal a todos los ambitos de las funciones anidadas a la primera
# 3. es asignada fuera de cualquier funcion esta es global al fichero en el que ha sido creada

# AMBITO DE UNA FUNCION
a = 'Python'    #SCOPE de la variable, global (al modulo)
print('Valor fuera, variable a = Python: ', a) 
def funcion():
    a = 33      #SCOPE local a la funcion
    print('Valor dentro, variable a = 33: ', a) 

funcion()

print('Valor fuera, variable a = Python: ', a)
## AMBITO DE UNA FUNCION