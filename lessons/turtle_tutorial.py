"""Turtle tutorial"""


from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()

# draw a square:
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)

# draw a square using a loop
# i: int = 0
# while (i < 4):
#     leo.forward(300)
#     leo.left(90)
#     i = i + 1

leo.penup()
leo.goto(-50, -50)
leo.pendown()

leo.pencolor("pink")
leo.fillcolor("pink")
leo.begin_fill()

# draw a triangle using a loop
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()

leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()

bob.speed(100) 

bob.penup()
bob.goto(-50, -50)
bob.pendown()

bob.pencolor(252, 89, 167)

side_length: int = 300

j: int = 0
while (j < 100):
    bob.forward(side_length)
    bob.left(123)
    side_length = side_length * .97
    j = j + 1

bob.hideturtle()

cat: Turtle = Turtle()

cat.speed(100)


done()