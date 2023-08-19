from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_POSITIONS=20

class Snake:

    def __init__(self):

        self.turtlesss=[]
        self.create_snake()
        self.head=self.turtlesss[0]
    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        tim = Turtle("turtle")
        tim.color("pink")
        tim.penup()
        tim.goto(position)
        self.turtlesss.append(tim)
    def extend_segment(self):
        self.add_segment(self.turtlesss[-1].position())
    def reset(self):
        for seg in self.turtlesss:
            seg.goto(1000,1000)
        self.turtlesss.clear()
        self.create_snake()
        self.head = self.turtlesss[0]



    def move(self):
        for seg_num in range(len(self.turtlesss) - 1, 0, -1):
            new_x = self.turtlesss[seg_num - 1].xcor()
            new_y = self.turtlesss[seg_num - 1].ycor()
            self.turtlesss[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_POSITIONS)
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)




