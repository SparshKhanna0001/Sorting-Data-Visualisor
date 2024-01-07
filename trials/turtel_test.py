import turtle

def draw_arrow(x, y, direction):
    arrow = turtle.Turtle()
    arrow.speed(0)
    arrow.color("green")
    arrow.pensize(3)
    arrow.penup()
    arrow.goto(x, y)
    arrow.pendown()

    if direction == 'y':
        arrow.setheading(180)
        arrow.left(135)
        arrow.forward(20)
        arrow.backward(20)
        arrow.right(90)
        arrow.forward(20)
        arrow.backward(20)
        arrow.left(45)
    elif direction == 'x':
        arrow.setheading(90)
        arrow.left(135)
        arrow.forward(20)
        arrow.backward(20)
        arrow.right(90)
        arrow.forward(20)
        arrow.backward(20)
        arrow.left(45)

    arrow.hideturtle()
    

#Example usage:
draw_arrow(50, 50, 'x')  # Call this function with your desired coordinates and direction
draw_arrow(20, 20, 'y')  # Call this function with your desired coordinates and direction
turtle.done()

"""Positional test functions; below"""

"""
#screen = turtle.Screen()
#screen.setup(width=950, height=800)  # Adjust dimensions as needed

# Create a turtle to draw the grid
grid_turtle = turtle.Turtle()
grid_turtle.speed(0)  # Set speed to fastest
grid_turtle.color("gray")  # Set grid color to gray
grid_turtle.pensize(1)  # Set grid line thickness

# Draw horizontal grid lines
for y in range(-300, 201, 25):  # Adjust spacing as needed
    grid_turtle.penup()
    grid_turtle.goto(-250, y)
    grid_turtle.pendown()
    grid_turtle.goto(250, y)

# Draw vertical grid lines
grid_turtle.left(90)  # Turn turtle to face vertically
for x in range(-300, 201, 25):  # Adjust spacing as needed
    grid_turtle.penup()
    grid_turtle.goto(x, -250)
    grid_turtle.pendown()
    grid_turtle.goto(x, 250)

# Hide the grid turtle
grid_turtle.hideturtle()

# Example usage: Draw a red square at (50, 50)
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.stamp()  # Stamp the square onto the grid
"""

