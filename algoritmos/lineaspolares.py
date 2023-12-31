#Importe de las librerias
import math
import matplotlib.pyplot as plt
#Array
Y_arreglo = []
X_arreglo = []

def main():
    print("Algoritmo lineas polares")
    x1 = int(input('Ingrese el valor del eje X1:'))
    y1 = int(input('Ingrese el valor del eje Y1:'))
    x2 = int(input('Ingrese el valor del eje X2:'))
    y2 = int(input('Ingrese el valor del eje Y2:'))
    m = abs(Pendiente(x1, x2, y1, y2))
    print("Pendiente: " + str(m))
    radianes = round(math.atan(m),4)
    grados = round(math.degrees(radianes),4)
    distancia = Distancia(x1,y1,x2,y2)
    coseno = round(math.cos(radianes),4)
    seno = round(math.sin(radianes),4)
    SegundoX = (float(distancia)* float(coseno))+x1
    SegundoY = (float(distancia)* float(seno))+ y1

    print("Radianes: " + str(radianes))
    print("Angulo:" + str(grados))
    print("Distancia (r): " + str(distancia))
    print("Coseno: " + str(coseno))
    print("Seno: " + str(seno))
    print("Segundo valor X: " + str(SegundoX))
    print("Segundo valor Y: "+ str(SegundoY))

    if(x1 < x2 and y1 < y2):
        Ejecucion(coseno,seno, distancia,x1,y1,1);
    elif (x1 > x2 and y1 > y2):
        Ejecucion(coseno,seno,distancia,x1,y1,2);
    elif (x1 < x2 and y1 > y2):
        Ejecucion(coseno, seno, distancia, x2, y2, 3)
    elif( x1 > y1 and y1 < y2):
        Ejecucion(coseno, seno, distancia, x1, y2, 4)
    rango_x = max(abs(x1),abs(x2));
    rango_y = max(abs(y1),abs(y2));
    showGrafic(rango_x,rango_y)

def Pendiente(x1,x2,y1,y2):
    m = (y2-y1)/(x2-x1);
    return m

def Distancia(x1,y1,x2,y2):
    delta_X = x2-x1
    delta_Y = y2-y1
    cuadradoA = pow(delta_X,2)
    cuadradoB = pow(delta_Y,2)
    raiz = math.sqrt(cuadradoA+cuadradoB)
    raiz = math.floor(raiz);
    
    return raiz

def Ejecucion(coseno,seno, distancia,x1,y1, opcion):
    x_inicio = math.floor(x1)
    y_inicio = math.floor(y1)
    print("| N | COS_D | COS | SEN | SEN_D |");
    print("| 0 |  "+ str(x1) + " |  " + str(x_inicio) + " |  " + str(y_inicio) + " |  "+ str(y1) + " |")
    X_arreglo.append(x1)
    Y_arreglo.append(y1)
    
    for n in range (distancia):
        if(opcion == 1):
            cos_decimal = round(x1 + coseno,4)
            sen_decimal = round(y1+seno,4)
        elif(opcion == 2):
            cos_decimal = round(x1 - coseno,4)
            sen_decimal = round(y1 - seno,4)
        elif(opcion == 3):
            cos_decimal = round(x1 - coseno,4)
            sen_decimal = round(y1 + seno,4)
        else:
            cos_decimal = round(x1 - coseno,4)
            sen_decimal = round(y1 + seno,4)
            
        residuoCos = cos_decimal%1;
        residuoSen = sen_decimal%1;
        
        if residuoCos <= 0.6:
            cos_entero = math.floor(cos_decimal);
        else:
            cos_entero = math.ceil(cos_decimal);
            
        if residuoSen <= 0.6:
            sen_entero = math.floor(sen_decimal);
        else:
            sen_entero = math.ceil(sen_decimal);
        
        X_arreglo.append(cos_entero)
        Y_arreglo.append(sen_entero)
        print("|"+str(n)+"|  "+ str(cos_decimal) + " |  " + str(cos_entero) + " |  " + str(sen_entero) + " |  "+ str(sen_decimal) + " |")
        x1 = cos_decimal
        y1 = sen_decimal

def showGrafic(rango_x,rango_y):
    #Preparamos la graficacion
    fig, ax = plt.subplots()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    print("\n\n")
    for i in range(len(X_arreglo)):
        print("Coordenada (" + str(X_arreglo[i])+","+str(Y_arreglo[i])+")");
                
    #Asignamos rangos
    ax.scatter(X_arreglo, Y_arreglo)
    plt.plot(X_arreglo, Y_arreglo)
    plt.xticks(range(-rango_x, rango_x+2,2))
    plt.yticks(range(-rango_y ,rango_y+2,2))       
    # Guardar el gráfico en formato png
    plt.savefig('Diagrama.png')
    # Mostrar el gráfico
    plt.show()

main();