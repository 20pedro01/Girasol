from turtle import *
import colorsys
import math

#Configuración inicial
speed(0.001)
bgcolor("black")
hideturtle()

#Dibujar los pétalos
def dibujar_petalos():
    goto(0, -40)
    for i in range(16):
        for j in range(18):
            c = colorsys.hsv_to_rgb(0.125, 1, 1)
            color(c)
            rt(90)
            circle(100 - j *4, 90)
            lt(90)
            circle(100 - j *4, 90)
            rt(180)
        circle(40, 24)

#Dibujar el centro de la flor
def dibujar_centro():
    color("black")
    shape("turtle")
    fillcolor("brown")
    phi = 137.508 * (math.pi/ 180.0)
    for i in range(200):
        r=2 * math.sqrt(i)
        theta = i * phi
        x= r * math.cos(theta)
        y= r * math.sin(theta)
        penup()
        goto(x, y)
        setheading(i * 137.508)
        pendown()
        stamp()

#Dibujar el tallo
def dibujar_tallo():
    penup()
    goto(0, -40)
    pendown()
    color("green")
    begin_fill()
    setheading(270)
    fd(250)
    lt(90)
    fd(10)
    lt (90)
    fd(250)
    lt(90)
    fd(10)
    end_fill()

#Dibujar cuadro de texto (opcional)
def dibujar_cuadro_texto():
    penup()
    #Nota: modificar todas las posiciones
    # de acuerdo al tamaño del texto
    goto(-250, 220)
    pendown()
    color("black")
    begin_fill()
    for _ in range(2):
        fd(300)
        rt(90)
        fd(50)
        rt(90)
    end_fill()

    penup()
    goto(-180, 230)
    pendown()
    color("white")
    write("        Escribe un mensaje aquí", font=("Arial", 16, "bold"))

#Orden en que se dibujará
dibujar_cuadro_texto()
dibujar_tallo()
dibujar_centro()
dibujar_petalos()

done()