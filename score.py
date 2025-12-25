from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,265)
        self.hideturtle()
        self.score=0
        self.score_board()

    def score_board(self):
        self.write(f"score={self.score}", align="center",font=("Arial",24,"normal"))

    def updates(self):
        self.score+=1
        self.clear()
        self.score_board()
        
      
    
    def game_end(self):
        self.goto(0,0)
        self.color("Red")
        self.write("GAME OVER", align="center",font=("Arial",24,"normal"))