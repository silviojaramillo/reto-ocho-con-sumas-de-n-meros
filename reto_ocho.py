######################################################################
#                           Reto número ocho                         #
# Contar y sumar los números naturales que son divisbles             #
# por 2 y por 7 dado un número máximo que debe ser ingresado         #
# por el usuario.                                                    #
# Nota: Mostrar los datos de manera ordenada en una pequeña tabla.   #
######################################################################
#Creando la variable para leer el número ingresado por el usaurio
#y el diccionario para guardar los datos.
number = int(input('Ingrese un número naturalo: '))
dictionary = {}

#Calculando los números que son divisibles entre 2 y 7
#y añadiéndolos al diccionario
for i in range(2,number + 1):
    if(i % 2 == 0 and i % 7 == 0):
        dictionary[str(i)] = i

#Contando los números del diccionario
size_dictionary = len(dictionary)

#Sumando los divisores de 2 y 7
plus_elements = 0
for j in dictionary:
    plus_elements = plus_elements + dictionary.get(str(j))

#Mostando los valores en la consola
print('Divisores       Suma de divisores        Conteo de divisores')
for x in dictionary:
    print(f"    {x}")
print(f"Totales               {plus_elements}                          {size_dictionary}")