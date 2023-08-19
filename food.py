
from turtle import Turtle
import random
class Food(Turtle):
    def __int__(self):
        super().__init__()

        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("grey")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.penup()
        random_x=random.randint(-300,300)
        random_y=random.randint(-300,300)
        self.goto(random_x,random_y)