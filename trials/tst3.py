import turtle

pen = turtle.Turtle()
pen.speed(0)

pen.penup()
pen.goto(-50, 50)  # Start at (-50, 50)
pen.pendown()

for _ in range(2):
    pen.forward(100)  # Width of 100 pixels
    pen.left(90)
    pen.forward(50)  # Height of 50 pixels
    pen.left(90)

pen.hideturtle()
turtle.done()
