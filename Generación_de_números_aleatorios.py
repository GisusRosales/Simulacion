#Alumno: Jesus Armando Rosales Martinez
#Matricula: 23040166
#Materia: Simulacion
#Grupo: 4Y
import random

def obtener_centrales(numero, longitud):
    numero_str = str(numero).zfill(longitud * 2)
    inicio = len(numero_str) // 4
    fin = inicio + longitud
    return int(numero_str[inicio:fin])

def centros_cuadrados(semilla, longitud, cantidad):
    numeros = []
    for _ in range(cantidad):
        cuadrado = semilla ** 2
        semilla = obtener_centrales(cuadrado, longitud)
        numeros.append(semilla)
    return numeros

def medios_cuadrados(semilla, longitud, cantidad):
    numeros = []
    for _ in range(cantidad):
        cuadrado = semilla ** 2
        semilla_str = str(cuadrado).zfill(longitud * 2)

        mitad_inicio = (len(semilla_str) - longitud) // 2
        semilla = int(semilla_str[mitad_inicio:mitad_inicio + longitud])
        numeros.append(semilla)
    return numeros

semilla = random.randint(1000, 9999)
longitud = 4
cantidad = 100

numeros_centros_cuadrados = centros_cuadrados(semilla, longitud, cantidad)
numeros_medios_cuadrados = medios_cuadrados(semilla, longitud, cantidad)

print("Números generados por el método de centros cuadrados:")
print(numeros_centros_cuadrados)

print("\nNúmeros generados por el método de medios cuadrados:")
print(numeros_medios_cuadrados)
