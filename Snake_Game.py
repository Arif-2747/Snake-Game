import turtle
import random

WIDTH = 500
HEIGHT = 500
DELAY = 100
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

score = 0
snake = [[0, 0], [0, 20], [0, 40]]
snake_direction = "up"

def reset():
    global snake, snake_direction, food_pos, score
    snake = [[0, 0], [0, 20], [0, 40]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    score = 0
    update_score()
    move_snake()

def move_snake():
    global snake_direction

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    if new_head in snake:
        game_over()
        return

    snake.append(new_head)

    if not food_collision():
        snake.pop(0)

    # screen wrapping
    if new_head[0] > WIDTH // 2:
        new_head[0] -= WIDTH
    elif new_head[0] < -WIDTH // 2:
        new_head[0] += WIDTH
    if new_head[1] > HEIGHT // 2:
        new_head[1] -= HEIGHT
    elif new_head[1] < -HEIGHT // 2:
        new_head[1] += HEIGHT

    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    screen.update()
    turtle.ontimer(move_snake, DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        score += 1
        update_score()
        return True
    return False

def get_random_food_pos():
    x = random.randint(-WIDTH//2 + 20, WIDTH//2 - 20)
    y = random.randint(-HEIGHT//2 + 20, HEIGHT//2 - 20)
    x = x // 20 * 20
    y = y // 20 * 20
    return (x, y)

def get_distance(pos1, pos2):
    return ((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2) ** 0.5

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

def game_over():
    pen.clear()
    pen.goto(0, 0)
    pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
    screen.update()

# Setup turtle screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()
pen.color("yellow")

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, HEIGHT//2 - 40)
score_writer.color("white")

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Start game
reset()
turtle.done()
