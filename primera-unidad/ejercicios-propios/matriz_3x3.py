"""
Desarrolla un programa en python que solicite al usuario los elementos de una matriz de 3x3 y despliegue:

a) La diagonal
b) La suma de los elementos de las 4 "puntas"
c) El promedio de todos sus elementos
d) La matriz original

"""

# Variables donde se controla de cuanto es la matriz, en este caso 3x3
filas = 3
columnas = 3
promedioTotal = 0
# Se inicializa con 0 los valores
matrizOriginal = [[0 for _ in range(columnas)] for _ in range(filas)]

for fila in range(filas):
    for columna in range(columnas):
        print(f"Dime el nuero de la fila {fila} con columna {columna}")
        matrizOriginal[fila][columna] = int(input())
        promedioTotal = matrizOriginal[fila][columna] + promedioTotal

# a) La diagonal
print("\nLos números diagonales son: ")
for i in range(len(matrizOriginal)):
    print(matrizOriginal[i][i], end= " ")
print()

# b) la suma de las puntas 
sumaPuntas = matrizOriginal[0][0] + matrizOriginal[0][-1] + matrizOriginal[-1][0] + matrizOriginal[-1][-1]
print(f"\nLa suma de las puntas es de: {sumaPuntas}")

# c) El promedio de todos sus elementos
promedioTotal = promedioTotal / (len(matrizOriginal) * 2)
print(f"\nEl promedio es de: {promedioTotal}")

# d) Matriz original print
for fila in matrizOriginal:
    print(fila)