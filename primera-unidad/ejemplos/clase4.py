#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:41:17 2023

@author: noracuevas
"""
# Definir la clase Estudiante
class Estudiante:
    # Método constructor para inicializar los atributos
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    # Método para mostrar información del estudiante
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Promedio: {self.promedio}")

    # Método para determinar si el estudiante está aprobado o no
    def esta_aprobado(self):
        if self.promedio >= 5.0:
            return True
        else:
            return False

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Juan", 20, 6.5)

# Llamar al método para mostrar información del estudiante
estudiante1.mostrar_informacion()

# Llamar al método para verificar si el estudiante está aprobado
if estudiante1.esta_aprobado():
    print("El estudiante está aprobado.")
else:
    print("El estudiante no está aprobado.")

