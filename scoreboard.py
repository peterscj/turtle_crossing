from turtle import Turtle

STYLE = ('Courier', 40, 'bold')
ALIGN = "center"
Y_COR = 240
X_COR = 0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Generates scoreboard output
        """
        self.clear()
        self.goto(X_COR, Y_COR)
        self.write(f"{self.level}",align=ALIGN,font=STYLE)

    def update_level(self):
        """
        Add 1 to score and clear text in scoreboard title
        """
        self.level += 1
        self.update_scoreboard()