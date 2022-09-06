from turtle import Turtle
FONT = ("Courier", 14, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.y = 0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.y} High score: {self.high_score}", move=False, align="center", font=FONT)

    def score_increase(self):
        self.y += 1
        self.score_update()

    def reset_sb(self):
        if self.y > self.high_score:
            self.high_score = self.y
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.y = 0
        self.score_update()
