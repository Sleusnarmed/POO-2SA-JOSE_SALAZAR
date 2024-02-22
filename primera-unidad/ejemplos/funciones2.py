#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:38:32 2023

@author: noracuevas
"""
# Definir una función para calcular el área de un rectángulo
def calcular_area_rectangulo(longitud, ancho):
    area = longitud * ancho
    return area

# Solicitar al usuario ingresar la longitud y el ancho del rectángulo
longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Llamar a la función y obtener el área
area_del_rectangulo = calcular_area_rectangulo(longitud, ancho)

# Imprimir el resultado

print("El área del rectángulo es:", area_del_rectangulo)