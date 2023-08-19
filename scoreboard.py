from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", "30", "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.color("Purple")
        self.penup()
        self.goto(0,100)
        self.hideturtle()
        self.aquaman()
    def aquaman(self):
        self.clear()
        self.write(f"Score is {self.score},High Score:{self.high_score}", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.aquaman()
    def function(self):
        self.score+=1
        self.aquaman()



