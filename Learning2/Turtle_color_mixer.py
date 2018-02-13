# colormixer

from turtle import Screen, Turtle, mainloop

class ColorTurtle(Turtle):

    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("arrow")
        self.resizemode("user")
        self.shapesize(3,3,5)
        self.pensize(10)
        self._color = [0,0,0]
        self.x = x
        self._color[x] = y
        self.color(self._color)
        self.speed(0)
        self.left(90)
        self.pu()
        self.goto(x,0)
        self.pd()
        self.sety(1)
        self.pu()
        self.sety(y)
        self.pencolor("gray25")
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(0,min(y,1)))
        self._color[self.x] = self.ycor()
        self.fillcolor(self._color)
        setbgcolor()

def setbgcolor():
    screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())
    screen.title("Red " + str(red.ycor())+"Green " + str(green.ycor())+"Blue " + str(blue.ycor()))

#    eraser = Turtle()
#    eraser.ht()
#    eraser.pu()
#    eraser.goto(1.0,1.08)
#    eraser.color((red.ycor(), green.ycor(), blue.ycor()))
#    eraser.shape('square')
##    eraser.resizemode("user")
#    eraser.shapesize(2.5,10)
#    eraser.showturtle()
#    del eraser
#    
#    writer = Turtle()
#    writer.ht()
#    writer.pu()
#    writer.goto(1,1.08)
#    writer.write("Red:" + str(red.ycor()),align="center",font=("Arial",10,("bold","italic"))) 
#    writer.ht()
#    writer.pu()
#    writer.goto(1,1.05)
#    writer.write("Green:" + str(green.ycor()),align="center",font=("Arial",10,("bold","italic"))) 
#    writer.ht()
#    writer.pu()
#    writer.goto(1,1.02)
#    writer.write("Blue:" + str(blue.ycor()),align="center",font=("Arial",10,("bold","italic"))) 
#    writer=''
#    del writer

def main():
    global screen, red, green, blue
    screen = Screen()
    screen.delay(0)
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)
    screen.tracer(8,25)


    red = ColorTurtle(0, .5)
    green = ColorTurtle(1, .5)
    blue = ColorTurtle(2, .5)

    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.goto(1,1.15)
    writer.write("DRAG!",align="center",font=("Arial",30,("bold","italic")))
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    for turtle in screen.turtles():
        turtle.color("Orange")
    mainloop()

