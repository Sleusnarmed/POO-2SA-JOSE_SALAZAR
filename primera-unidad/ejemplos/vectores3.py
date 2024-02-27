#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:33:37 2023

@author: noracuevas
"""
# Crear dos vectores como listas
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Imprimir los vectores
print("Vector 1:", vector1)
print("Vector 2:", vector2)

# Suma de vectores
suma_vector = [vector1[i] + vector2[i] for i in range(len(vector1))]
print("Suma de vectores:", suma_vector)

# Multiplicación por un escalar
escalar = 2
multiplicacion_vector = [escalar * elemento for elemento in vector1]
print("Multiplicación por un escalar:", multiplicacion_vector)
