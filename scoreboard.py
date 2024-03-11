from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.goto(x=-290,y=270)
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)
        
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write('GAME OVER', align='center', font=FONT)