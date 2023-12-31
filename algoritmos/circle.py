#Importar librerias
import matplotlib.pyplot as plt

coordenadas = []
# calcular Circunferencia con punto medio
def calcular(x_center, y_center, radio):
    x = 0
    y = radio
    p = 5/4 - radio

    while x <= y:
        if p < 0:
            p += 2 * x + 1
            x += 1
        else:
            p += 2 * (x - y) + 1
            x += 1
            y -= 1

        print(f'({x},{y})')
        #mostrar puntos
        plt.plot(x,y, 'ro')
        plt.plot(x,-y, 'ro')
        plt.plot(-x,y, 'ro')
        plt.plot(-x,-y, 'ro')
        plt.plot(y,x, 'ro')
        plt.plot(y,-x, 'ro')
        plt.plot(-y,x, 'ro')
        plt.plot(-y,-x, 'ro')

def main():
    x = int(input(print("Valor de X: ")))
    y = int(input(print("Valor de Y: ")))
    r = int(input(print("Valor de Radio: ")))

    plt.title("Circunferencia")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, y, 'ro')
    calcular(x, y, r)

    plt.show()
if __name__ == '__main__':
    main()