#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:42:19 2023

@author: noracuevas
"""
class Persona:
    def establecer_datos(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"calificacion: {self.calificacion}")

# Crear un objeto de la clase Persona
persona1 = Persona()

# Establecer los datos de la persona
persona1.establecer_datos("Juan", 25, 90)

# Mostrar la información de la persona
persona1.mostrar_informacion()


persona2 = Persona()

# Establecer los datos de la persona
persona2.establecer_datos("Jorge", 50, 60)

# Mostrar la información de la persona
persona2.mostrar_informacion()


persona3 = Persona()

# Establecer los datos de la persona
persona3.establecer_datos("Alicia", 37, 95)

# Mostrar la información de la persona
persona3.mostrar_informacion()