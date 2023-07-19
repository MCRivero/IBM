# La sintaxis del bucle for es muy sencilla y parecida a la del bucle while, con la excepción que en la 
# cabecera del for, en lugar de evaluar una expresión en cada iteración, vamos asignando elementos de un 
# iterador a una variable.
a = 0
for x in [1, 2, 3, 4]:
    a += x
print(a)

for elem in ['Me', 'gusta', 'Python!']:
    print(elem, end = ' ')

print('\n---------------------------')

for elem in 'Me gusta Python!':
    print(elem, end = ' ')


# Veamos un ejemplo recorriendo un diccionario, ya que uno de los usos más frecuentes 
# del bucle for es recorrer objetos iterables, diccionarios, tuplas…etc: