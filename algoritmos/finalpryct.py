import turtle as t
t.pensize(10)
#Determina el color del circulo
t.fillcolor('yellow')
t.hideturtle()
#Determina el color del fondo
t.bgcolor('pink')

#Circulo
radius=180
t.penup()
t.setposition(0,-radius)
t.setheading(0)
t.pendown()
t.begin_fill()
t.circle(radius)
t.end_fill()
 #Linea de sonrisa
colormouth = 'red'
mouth_radius=radius*0.6
mouth_angle= 90
t.pencolor (colormouth)
t.penup()
t.setposition(0, -mouth_radius)
t.setheading(0)
t.pendown()
t.circle(mouth_radius,mouth_angle)
t.penup()
t.setposition(0,-mouth_radius)
t.setheading(0)
t.pendown()
t.circle(mouth_radius,-mouth_angle)


#Posicion de los ojos
x=50
y=50
#Tamaño de los ojos
eye_size=60
color = 'white'
t.penup()
t.setposition(x,y)
t.pendown()
t.dot(eye_size, color)
t.penup()
t.setposition(-x,y)
t.dot(eye_size, color)
t.done()

