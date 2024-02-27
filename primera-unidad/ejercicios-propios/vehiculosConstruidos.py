"""
Desarrolla un programa en Python para calcular el rendimiento de gasolina de 3 vehículos
Para calcular el rendimiento:
    -Capacidad del tanque del vehiculo 1-30 lts
    -Cuantos kilmetros recorre con 5lts
"""
class Vehiculo:
    def __init__(self, capacidad_tanque, km_recorridos):
        self.capcacidad_tanque = capacidad_tanque
        self.km_recorridos = km_recorridos
        self.rendimiento = (capacidad_tanque * km_recorridos) / 5

    def mostrar_informacion(self):
        print(f"La capacidad del tanque: {self.capcacidad_tanque}")
        print(f"Los kilometros que recorre con 5lts: {self.km_recorridos}")
        print(f"El rendimiento: {self.rendimiento}")
        
vehiculos_a_construir = int(input("Cuantos vehiculos vas a construir?"))


def creacion_vehiculos(vehiculos_a_construir):
    vehiculos_construidos = []
    for i in range(vehiculos_a_construir):
        print(f"Ingrese los datos del vehículo {i + 1}:")
        capacidad = float(input("Capacidad del tanque: "))
        km = float(input("Los kilometros que recorre con 5lts: "))
        vehiculo = Vehiculo(capacidad, km)
        vehiculos_construidos.append(vehiculo)
    return vehiculos_construidos

def mostrar_vehiculos(vehiculos_construidos):
    for i, vehiculo in enumerate (vehiculos_construidos):
        print(f"\nInformación del vehiculo {i + 1} : ")
        vehiculo.mostrar_informacion()

vehiculos = creacion_vehiculos(vehiculos_a_construir)

mostrar_vehiculos(vehiculos)