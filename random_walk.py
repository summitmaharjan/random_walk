from turtle import Turtle, Screen
import random

t = Turtle()

colors = ["lime green", "dark orange", "green yellow", "gold", "dark violet", "red"]
direction = [0, 90, 180, 270]
t.speed(10)
for _ in range(50):
    t.pensize(10)
    t.forward(20)
    t.color(random.choice(colors))
    t.setheading(random.choice(direction))

s= Screen()
s.exitonclick()