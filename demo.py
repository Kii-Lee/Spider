import turtle
import random
color = ["red","green","blue","orange"]
t = turtle.Turtle()
t.width(4)
for i in range(12):
    t.right(30)
    t.color(color[random.randint(0,3)])
    for i in range(8):
        t.forward(100)
        t.right(45)
turtle.mainloop()