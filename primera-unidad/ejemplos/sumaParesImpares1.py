#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:29:32 2023

@author: noracuevas
"""
# Solicitar al usuario un número entero positivo n
n = int(input("Ingrese un número entero positivo: "))

# Inicializar variables para la suma de números pares e impares
suma_pares = 0
suma_impares = 0

# Calcular la suma de números pares e impares en el rango del 1 al n
# Utilizamos un bucle for para iterar sobre los números en el rango
for numero in range(1, n + 1):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

# Imprimir las sumas por separado
print("Suma de números pares:", suma_pares)
print("Suma de números impares:", suma_impares)