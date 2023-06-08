import turtle

class messages:
    def __init__(self):
        self.messageTurtle = []
        newturtle = turtle.Turtle()
        newturtle.up()
        newturtle.speed(0)
        newturtle.hideturtle()
        self.messageTurtle.append(newturtle)
    
    def draw(self, message, apple_count):
        self.messageTurtle[0].write(message,align="center",font=("Arial",24,"normal"))
        self.messageTurtle[0].goto(self.messageTurtle[0].xcor(),self.messageTurtle[0].ycor()-100)
        self.messageTurtle[0].write(apple_count,align="center",font=("Arial",24,"normal"))