
lista1 = [4, 3, 6, 4]

# añadir elementos
lista1.append(3)
# contar elementos del dado por parámetro
a = lista1.count(3)
# longitud de la lista
print(len(lista1))
# Devuelve el índice (posición) del valor especificado
print("Indice de 6:", lista1.index(6))
# Acceder a un elemento dado el índice [0, n-1] siendo n la longitud de la lista
print(lista1[3])
# Remove elimina el primer elemento específicado
lista1.remove(4)
print(lista1)
