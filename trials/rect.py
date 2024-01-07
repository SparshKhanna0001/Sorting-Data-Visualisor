import turtle

def create_rounded_rectangle(x, y, width, height, fill_color, outline_color="black"):
    """
    Creates a rounded rectangle with the given specifications.

    Args:
        x: The x-coordinate of the starting position.
        y: The y-coordinate of the starting position.
        width: The width of the rectangle.
        height: The height of the rectangle.
        fill_color: The color to fill the rectangle with.
        outline_color: The color of the outline (default: black).
    """

    pen = turtle.Turtle()
    pen.speed(0)  # Fastest speed
    pen.pensize(1)  # Thicker outline

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.fillcolor(fill_color)
    pen.begin_fill()

    # Draw rounded corners using a series of arcs
    for _ in range(2):
        pen.forward(width - 50)  # Adjust for corner arcs
        pen.circle(25, 90)  # Create a quarter-circle arc
        pen.forward(height - 50)
        pen.circle(25, 90)
    
    pen.end_fill()
    """
    pen.pencolor(outline_color)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    """
    """
    # Retrace the outline for a thicker and smoother appearance
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    """

    pen.hideturtle()

# Example usage:
create_rounded_rectangle(-50, 50, 150, 100, "lightblue")  # Create a light blue rectangle
turtle.done()  # Keep the window open
