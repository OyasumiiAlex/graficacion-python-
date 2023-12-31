import matplotlib.pyplot as plt
print("Inserte el valor en x1: ")
x1 = float(input())
print("Inserte el valor en  x2: ")
x2 = float(input())
print("Inserte el valor en  y1: ")
y1 = float(input())
print("Inserte el valor en  y2: ")
y2 = float(input())

#Calculo de la diferencia entre los valores de pixel de inicio y destino
dx = x2 - x1
dy = y2 - y1

#Si DX es mayor a DY entonces:

if abs(dx) > abs(dy):
    interaciones = abs(dx)
else:
    interaciones = abs(dy)

xincrement = dx/interaciones
yincrement = dy/interaciones

i = 0

xcoordinates = []
ycoordinates = []


while i < interaciones:
    i +=1
    x1 = x1 + xincrement
    y1 = y1 + yincrement
    print("X1: ",x1, "Y1: ", y1)
    xcoordinates.append(x1)
    ycoordinates.append(y1)

plt.plot(xcoordinates, ycoordinates)

#Naming the Axis
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

#Graph title
plt.title("Algoritmo DDA (analizador diferencial digital)")

#show the plot

plt.show()