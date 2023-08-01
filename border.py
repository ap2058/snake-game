import turtle

# Function to draw a rectangle
def draw_rectangle(width, height):
    turtle.penup()
    turtle.goto(-width/2, height/2)
    turtle.pendown()

    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def main():
    # Set up the turtle window
    screen = turtle.Screen()
    screen.setup(520, 520)  # Add some extra pixels for borders
    screen.title("Drawing a Rectangle with Turtle")
    screen.bgcolor("white")

    # Create a turtle object
    t = turtle.Turtle()

    # Set the turtle speed
    t.speed(1)

    # Draw a rectangle with width and height of 500 each
    draw_rectangle(500, 500)

    # Keep the window open until manually closed
    turtle.done()

if __name__ == "__main__":
    main()