#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:36:41 2024

@author: noracuevas
"""

#No existe la sobrecarga de métodos en Python
#En Java si se puede

class OperacionesMatematicas:
    def suma(self, a, b):
        return a + b

    def suma(self, a, b, c):
        return a + b + c

# Crear una instancia de la clase
operaciones = OperacionesMatematicas()

# Llamar a los métodos sobrecargados
resultado_suma_dos_numeros = operaciones.suma(2, 3)
resultado_suma_tres_numeros = operaciones.suma(2, 3, 4)

print("Resultado de la suma de dos números:", resultado_suma_dos_numeros)
print("Resultado de la suma de tres números:", resultado_suma_tres_numeros)