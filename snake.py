from turtle import Turtle


UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake :
    def __init__(self):
        self.snakelist = []
        self.create_snake()
        self.head = self.snakelist[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")
        turtle.setpos(position)
        self.snakelist.append(turtle)

    def extend(self):
        self.add_segment(self.snakelist[-1].position())


    def move(self):
        for s in range(len(self.snakelist) - 1, 0, -1):
            new_x = self.snakelist[s - 1].xcor()
            new_y = self.snakelist[s - 1].ycor()
            self.snakelist[s].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            pass
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            pass
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            pass
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            pass