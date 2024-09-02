import turtle as t
import random
t= Turtle()
t.shape('turtle')
t.color('blue')
color = ['medium aquamarine','deep pink','dark magenta','light coral','orange','saddle brown','hot pink','dark green','medium blue']


#task 2 draw a dashed line
for i in range (40):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


#task 3 drawing different shapes with random color
def repeat(n):
  angle = 360/n
  for i in range(n):
    t.forward(50)
    t.right(angle)
for i in range(4,11):
  t.color(random.choice(color))
  repeat(i)


#Task 4 Random Walk with random speed, thickness and random color

directions = [0,90,180,270]
speed = range(0,11)
pensize = range(0,11)
def random_walk():
    t.setheading(random.choice(directions))
    t.speed(random.choice(speed))
    t.color(random.choice(color))
    t.pensize(random.choice(pensize))
    t.forward(10)
while True:
    random_walk()


#Task 5 random color with RGB colours
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
  
 t.color(random_color())
#Task 6 Make a Spirograph
for i in range(0,360,10):
    t.color(random_color())
    t.circle(100)
    t.setheading(i)




screen=Screen()
screen.exitonclick()
