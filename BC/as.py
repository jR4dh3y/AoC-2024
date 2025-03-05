import turtle
import time
import random

def draw_cake():
    turtle.penup()
    turtle.goto(-75, -50)
    turtle.pendown()
    turtle.color("chocolate")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.color("pink")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

def draw_candles():
    candle_colors = ["red", "blue", "yellow", "green", "purple"]
    for i in range(-40, 60, 40):
        turtle.penup()
        turtle.goto(i, 100)
        turtle.pendown()
        turtle.color(random.choice(candle_colors))
        turtle.begin_fill()
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.end_fill()
        draw_flame(i + 5, 130)

def draw_flame(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("orange")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

def show_message(name):
    turtle.penup()
    turtle.goto(0, -150)
    turtle.color("purple")
    turtle.write(f"Happy Birthday, {name}!", align="center", font=("Arial", 24, "bold"))

def birthday_surprise(name):
    turtle.setup(600, 400)
    turtle.bgcolor("lightblue")
    turtle.speed(3)
    draw_cake()
    draw_candles()
    show_message(name)
    time.sleep(5)
    turtle.bye()

if __name__ == "__main__":
    name = "tanuska"
    birthday_surprise(name)
