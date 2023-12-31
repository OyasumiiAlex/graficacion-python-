import math
import matplotlib.pyplot as plt
"""
4 lados iguales * interiores de 90°
Formula
Xn = distancia * cosAngl° + Xn
Yn = distancia * senAngl° + Yn

"""
#Input del X&Y
print("Inserte los valores:")
print("x1:")
x0 = int(input())
print("y1:")
y0 = int(input())

#Input de la distancia
print(" Distancia:")
d = int(input())

#Input del angulo 
print(" Angulo:")
angl = int(input())

print("x: ", x0)
print("y: ", y0)

#Calculo del punto X1
x1 = d * math.cos(math.radians(angl)) + x0
y1 = d * math.sin(math.radians(angl)) + y0
angl = angl + 90

print("x1: ", x1)
print("y1: ", y1)

#Calculo del punto X2
x2 = d * math.cos(math.radians(angl)) + x1
y2 = d * math.sin(math.radians(angl)) + y1
angl = angl + 90

print("x2: ", x2)
print("y2: ", y2)

#Calculo del punto X3
x3 = d * math.cos(math.radians(angl)) + x2
y3 = d * math.sin(math.radians(angl)) + y2
angl = angl + 90
print("x3: ", x3)
print("y3: ", y3)

plt.plot([x0, x1, x2, x3, x0], [y0, y1, y2, y3, y0])

plt.show()