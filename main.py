import turtle
import random

WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 20
DELAY = 100  # milliseconds
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# Global variables for the game
snake = []
snake_direction = "up"
food_pos = (0, 0)
score = 0
highest_score = 0

def reset():
    global snake, snake_direction, food_pos, score, highest_score
    snake = [[0, 0], [0, 20], [0, 40], [0, 50], [0, 60]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    score = 0  # Reset the score at the start of a new game
    gamedetails()
    update_score_display()
    move_snake()

def move_snake():
    global snake_direction, score, highest_score, food_pos
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_direction][0]
    new_head[1] = snake[-1][1] + offsets[snake_direction][1]

    # Check self-collision
    if new_head in snake[:-1]:  # Or collision with walls?
        reset()
    else:
        # No self-collision so we can continue moving the snake.
        snake.append(new_head)

        # Check food collision
        if food_collision():
            score += 10
            if score > highest_score:
                highest_score = score
            update_score_display()
            food_pos = get_random_food_pos()
            food.goto(food_pos)

        else:
            snake.pop(0)  # Keep the snake the same length unless fed.

        # Allow screen wrapping
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < -WIDTH / 2:
            snake[-1][0] += WIDTH
        elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT

        # Clear previous snake stamps
        pen.clearstamps()

        # Draw snake
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        # Refresh screen
        screen.update()

        # Rinse and repeat
        turtle.ontimer(move_snake, DELAY)

def food_collision():
    global food_pos
    if get_distance(snake[-1], food_pos) <= FOOD_SIZE:
        return True
    return False

def get_random_food_pos():
    x = random.randint(-WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def update_score_display():
    pen.clear()
    pen.goto(-WIDTH // 2 , HEIGHT // 2 )
    pen.color("green")
    pen.write(f"Score: {score}  Highest Score: {highest_score}", align="left", font=("Courier", 12, "normal"))

def gamedetails():
    pen.clear()
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake game by Aashish")
screen.bgcolor("white")


screen.setup(500, 500)
screen.tracer(2)

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("black")
food.shapesize(FOOD_SIZE / 30)
food.penup()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
turtle.done()
