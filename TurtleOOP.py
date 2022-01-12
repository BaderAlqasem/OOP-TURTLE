import turtle

screen_height = 600
screen_width = 600
screen = turtle.Screen()
gameScreen = screen.setup(screen_width, screen_height)



screen.bgcolor("#34abeb")
screen.title("Game")

class Player(turtle.Turtle):

  def __init__(self):
    turtle.Turtle.__init__(self)
    self.penup()
    self.shape("turtle")
    self.color("green")
    self.speed = 0
    

  def move(self):
    self.forward(self.speed)
    
  def turnLeft(self):
    self.left(45)
    
  def turnRight(self):
    self.right(45)
        
  def increaseSpeed(self):
    self.speed +=1
      
  def decreaseSpeed(self):
    self.speed -=1
    
def clearScreen():
    player.clear()


player = Player()
playerSize = 20


player.goto(playerSize/2 - screen.window_width()/2, screen.window_height()/2 - playerSize/2)
player.pencolor("black")
player.pendown()
player.showturtle()


turtle.listen()
artist = turtle

artist.onkey(player.turnLeft, "a")
artist.onkey(player.turnRight, "d")
artist.onkey(player.increaseSpeed, "w")
artist.onkey(player.decreaseSpeed, "s")
artist.onkey(clearScreen, "c")


loop = True

while loop == True:
    player.move()
