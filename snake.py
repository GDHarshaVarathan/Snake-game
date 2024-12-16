from turtle import Turtle, Screen
from food import Food
from scoreboard import Score
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180
score=Score()
food=Food()
screen=Screen()
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)    
        self.segments[0].forward(20)
    def move_up(self):
        if  self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(90)
    def move_down(self):
        if self.segments[0].heading()!=UP:
            self.segments[0].setheading(270)
    def move_right(self):
        if self.segments[0].heading()!=LEFT:
            self.segments[0].setheading(0)
    def move_left(self):
        if self.segments[0].heading()!=RIGHT:
            self.segments[0].setheading(180)
    def take_food(self):
        if food.distance(self.segments[0])<15:
            food.refresh()
            score.increase_score()
            self.extend()
    def detect_head(self,head):
       for i in range(len(self.segments)):
           head.append(self.segments[i])
           
            
            
