from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments=[]
        self.position=[(0,0),(-20,0),(-40,0)]
        self.make_snake()
        self.head=self.segments[0]

    def make_snake(self):
        for cor in self.position:
            self.add_segment(cor)
    
    def add_segment(self,cor):
        segment=Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(cor)
        self.segments.append(segment)

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

    def move_snake(self):
        for segment in range(len(self.segments)-1,0,-1):
            x_cor=self.segments[segment-1].xcor()
            y_cor=self.segments[segment-1].ycor()
            self.segments[segment].goto(x_cor,y_cor)
        self.segments[0].forward(20)

    def expand(self):
        self.add_segment(self.segments[-1].position())


    






