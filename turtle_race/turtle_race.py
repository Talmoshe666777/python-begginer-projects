import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'brown', 'cyan']
random.shuffle(COLORS)


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')


def get_number_of_turtles():
    turtles = 0
    while True:
        turtles = input("Enters the number pf turtles (2-10): ")
        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print("Input is not numeric... try again")
            continue
        if 2 <= turtles <= 10:
            return turtles
        else:
            print("Input is not in range")


number_of_turtle = get_number_of_turtles()
colors = COLORS[:number_of_turtle]
init_turtle()


def create_racers(colors):
    # Difference between forward & backward to left & right is that right+left get angle degree and the others pixels
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colors):
    turtles = create_racers(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


winner = race(colors)
print(f"The winner is the {winner} turtle")
