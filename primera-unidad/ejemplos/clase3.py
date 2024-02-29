#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:39:47 2023

@author: noracuevas
"""
class Rectangulo:
    # Constructor de la clase Rectangulo
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    
    # Método para calcular el área del rectángulo
    def calcular_area(self):
        return self.longitud * self.ancho
    
    # Método para calcular el perímetro del rectángulo
    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)

# Crear un objeto de la clase Rectangulo
mi_rectangulo = Rectangulo(5, 3)

# Acceder a los atributos y métodos del objeto
print("Longitud del rectángulo:", mi_rectangulo.longitud)
print("Ancho del rectángulo:", mi_rectangulo.ancho)
print("Área del rectángulo:", mi_rectangulo.calcular_area())
print("Perímetro del rectángulo:", mi_rectangulo.calcular_perimetro())
