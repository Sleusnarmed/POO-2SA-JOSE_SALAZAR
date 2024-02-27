#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:27:50 2023

@author: noracuevas
"""
# Definir dos matrices
matriz_A = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matriz_B = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

# Inicializar una matriz para almacenar el resultado
filas_A = len(matriz_A)
columnas_A = len(matriz_A[0])
filas_B = len(matriz_B)
columnas_B = len(matriz_B[0])

# Verificar si es posible multiplicar las matrices
if columnas_A != filas_B:
    print("No se pueden multiplicar las matrices. El número de columnas de A debe ser igual al número de filas de B.")
else:
    # Inicializar una matriz de resultados con ceros
    resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    # Realizar la multiplicación de matrices
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += matriz_A[i][k] * matriz_B[k][j]

    # Imprimir el resultado
    print("Matriz A:")
    for fila in matriz_A:
        print(fila)

    print("\nMatriz B:")
    for fila in matriz_B:
        print(fila)

    print("\nResultado de la multiplicación:")
    for fila in resultado:
        print(fila) 