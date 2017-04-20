import turtle, math, random

def random_color():
  r = lambda: random.randint(0,255)
  return ('#%02X%02X%02X' % (r(),r(),r()))

def initialize_myturtle(fillcolor):

  new_turtle = turtle.Turtle()
  new_turtle.hideturtle()
  new_turtle.penup()
  new_turtle.setpos(-200, -200)
  new_turtle.shape("turtle")
  new_turtle.speed(10) 
  new_turtle.fillcolor(fillcolor)

  return new_turtle

def draw_triangle(the_turtle,size):

  if size < 5:
    return

  the_turtle.showturtle()
  the_turtle.pendown()
  the_turtle.begin_fill()
  for i in range(3):
    the_turtle.forward(size)
    the_turtle.left(360/3)

  the_turtle.end_fill()
  the_turtle.penup()
  the_turtle.hideturtle()

  size = size/2.0
  xcor = the_turtle.xcor()
  ycor = the_turtle.ycor()
  #draw left triangle
  the_turtle.left(360/3)
  the_turtle.forward(size)
  the_turtle.right(360/3)
  draw_triangle(the_turtle, size) 

  #draw right triangle
  the_turtle.setpos(xcor,ycor)
  the_turtle.right(360/6)
  the_turtle.forward(size)
  the_turtle.left(360/6)
  draw_triangle(the_turtle, size) 

  #draw top triangle
  the_turtle.setpos(xcor,ycor)
  the_turtle.left(360/12) 
  the_turtle.forward(size*math.sqrt(3.0))
  the_turtle.right(360/12)
  draw_triangle(the_turtle, size)

  return

def draw_fractal():

  fullsize = 416
  c_size = fullsize
  window = turtle.Screen()
  dark_color = random_color()
  light_color = "white"

#level 1 colored shape
  my_turtle1 = initialize_myturtle(dark_color)
  my_turtle1.showturtle()
  my_turtle1.pendown()
  my_turtle1.begin_fill()
  for i in range(3):
    my_turtle1.forward(fullsize)
    my_turtle1.left(360/3)

  my_turtle1.end_fill()
  my_turtle1.penup()
  my_turtle1.hideturtle()


  my_turtle1 = initialize_myturtle(light_color)
  c_size = c_size/2.0
  my_turtle1.forward(c_size)
  my_turtle1.left(360/6)

  draw_triangle(my_turtle1, c_size)

  window.exitonclick()


draw_fractal()