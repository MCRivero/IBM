def suma(a,b): 
    return a+b

print(suma(2,3))
print(suma(40,30))

print('----------------------')

# Ejemplo de objetos inmutables
# OBJETO INMUTABLE: NO PUEDE CAMBIAR SU VALOR DESPUES DE SU CREACION
print('OBJETO INMUTABLE')
def suma(a, b): #Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b 

a, b = 5, 10
print(suma(a, b))   #El resultado de llamar a suma sera 7. Toma los valores definidos dentro de la funcion
print(a, b)         #El resultado será 5 10. Toma los valores asignados fuera de la funcion
print('----------------------')

#Ejemplo de objeto mutable
def minimo(l):
    l[0] = 1000     #Modificamos la lista en el interior
    return min(l)

l = [1, 2, 3]
print('LISTA : ', l)

print('LLAMADA FUNCION MINIMO: ', minimo(l))
print(l)

# ENTENDER RESULTADO PAGINA 11-12 