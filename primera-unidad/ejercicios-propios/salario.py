"""
Desarrolla un programa en python para calcular el saario final de N empleados

sueldo = horas trabajadas * sueldo por hora
impuestos = 5% del sueldo
prestaciones = 10% de sueldo

salario final = sueldo + prestaciones - impuestos

"""
class Empleados:
    def __init__(self, horas_trabajadas, sueldo_hora):
        self.horas_trabajadas = horas_trabajadas
        self.sueldo_hora = sueldo_hora
        self.sueldo = horas_trabajadas * sueldo_hora
    
    def calcular_sueldo(self):
        print(self.sueldo + (self.sueldo * 0.10) - (self.sueldo * 0.05))

empleados_a_calcular = int(input("Dime a cuantos empleados se le calculará el sueldo final"))

# n = empleados a calcular
def lista_sueldo(n):
    sueldo_de_empleados = []
    for i in range(n):
        print(f"Ingrese los datos del vehículo {i + 1}:")
        horas_trabajadas = float(input("Dime las horas trabajadas "))
        sueldo_hora = float(input("Dime el sueldo por hora que recibe "))
        empleado = Empleados(horas_trabajadas, sueldo_hora)
        sueldo_de_empleados.append(empleado)
    return sueldo_de_empleados

def mostrar_sueldo(sueldo_de_empleados):
    for i, empleado in enumerate (sueldo_de_empleados):
        print(f"\nInformación del vehiculo {i + 1} : ")
        empleado.calcular_sueldo()

empleados = lista_sueldo(empleados_a_calcular)
mostrar_sueldo(empleados)