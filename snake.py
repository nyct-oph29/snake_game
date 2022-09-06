from turtle import Turtle
MOVE_DISTANCE = 20
TURN = [0, 90, 180, 270]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        y = 0
        for _ in range(3):
            turtle = Turtle("square")
            self.segments.append(turtle)
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=y, y=0)
            y -= 20

    def reset(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != TURN[3]:
            self.head.setheading(TURN[1])

    def down(self):
        if self.head.heading() != TURN[1]:
            self.head.setheading(TURN[3])

    def left(self):
        if self.head.heading() != TURN[0]:
            self.head.setheading(TURN[2])

    def right(self):
        if self.head.heading() != TURN[2]:
            self.head.setheading(TURN[0])

    def add_length(self):
        position = self.segments[-1].position()
        turtle = Turtle("square")
        self.segments.append(turtle)
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)

