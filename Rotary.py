from turtle import *
import colorsys

bgcolor('black')
speed(0)
delay(0)
colormode(1.0)  # Use RGB colors scaled 0-1 instead of 0-255

h = 0

def draw():
    global h
    for i in range(100):
        c = colorsys.hsv_to_rgb(h % 1.0, 1, 1)  # HSV to RGB conversion with hue wrapping
        h += 0.01
        up()
        goto(0, 0)
        down()
        color('black', c)  # Pen color = black, fill color = c
        begin_fill()
        rt(98)
        circle(i, 12)
        fd(100)
        lt(29)
        for j in range(10):
            fd(i)
            circle(j, 50, steps=2)
        end_fill()
draw()
done()
