import turtle

def button_click(x, y):
    print("Button clicked!")  # Replace with actual button actions

turtle.setup(width=400, height=300)

# Create a button
button_turtle = turtle.Turtle()
button_turtle.penup()
button_turtle.goto(-50, 0)
button_turtle.begin_fill()
button_turtle.fillcolor("lightblue")
button_turtle.pendown()
for _ in range(2):
    button_turtle.forward(100)
    button_turtle.left(90)
    button_turtle.forward(40)
    button_turtle.left(90)
button_turtle.end_fill()
button_turtle.penup()
button_turtle.goto(-25, 15)
button_turtle.write("Click Me", align="center", font=("Arial", 12, "normal"))

turtle.onscreenclick(button_click)
turtle.done()
