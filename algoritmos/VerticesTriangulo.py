'''
Examen final: Sergio Alexander Hernandez Mendez 

Calcular los vertices de un triangulo con los siguientes datos
Parametros: 
1.-Un punto (X&Y)
2.-Dos angulos 
3.-Dos distancias

Datos a tomar en cuenta:

P0 (70,50)
1 angulo: 25°
D1= 30
2 angulo: 60°
D2= 45
'''
#Importar librerias
import math
import matplotlib.pyplot as plt

#Calculo de punto X
def calcular_x(distancia, angulo, x):
    return distancia * math.cos(math.radians(angulo)) + x

#Calculo del punto Y
def calcular_y(distancia, angulo, y):
    return distancia * math.sin(math.radians(angulo)) + y

#Main
def main():
    # Puntos del triangulo
    p0 = []
    p1 = []
    p2 = []

    #Variables del triangulo
    angulo1 = 0
    angulo2 = 0
    distancia1 = 0
    distancia2 = 0
    #Inpunt en consola
    print("-----Datos del P0-----")
    p0.append(int(input("x: ")))
    p0.append(int(input("y: ")))

    angulo1 = int(input("Angulo 1: "))
    distancia1 = int(input("Distancia 2: "))

    angulo2 = int(input("Angulo 2: "))
    distancia2 = int(input("Distancia 2: "))

    #Algoritmo
    p1.append(calcular_x(distancia1, angulo1, p0[0]))
    p1.append(calcular_y(distancia1, angulo1, p0[1]))
    print(p1[0], p1[1])

    p2.append(calcular_x(distancia2, angulo2, p1[0]))
    p2.append(calcular_y(distancia2, angulo2, p1[1]))
    print(p2[0], p2[1])

    plt.title("Examen Final Triangulo")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.plot([p0[0], p1[0], p2[0], p0[0]], [p0[1], p1[1], p2[1], p0[1]])

    plt.show()


main()