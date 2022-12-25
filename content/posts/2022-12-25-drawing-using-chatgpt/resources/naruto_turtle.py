import turtle

# Create a new turtle object
t = turtle.Turtle()

# Set the turtle's speed to the maximum value (10)
t.speed(10)

# Set the turtle's pen color to orange
t.pencolor("orange")

# Set the turtle's pen size to 3
t.pensize(3)

# Set the turtle's starting position
t.penup()
t.setpos(-100, 0)
t.pendown()

# Draw the head
t.circle(50)

# Move the turtle to the position for the body
t.penup()
t.setpos(-50, -50)
t.pendown()

# Draw the body
t.forward(100)

# Move the turtle to the position for the arms
t.penup()
t.setpos(-75, -25)
t.pendown()

# Draw the left arm
t.left(45)
t.forward(50)

# Move the turtle to the position for the right arm
t.penup()
t.setpos(-25, -25)
t.pendown()

# Draw the right arm
t.right(90)
t.forward(50)

# Move the turtle to the position for the legs
t.penup()
t.setpos(-65, -100)
t.pendown()

# Draw the left leg
t.left(45)
t.forward(50)

# Move the turtle to the position for the right leg
t.penup()
t.setpos(-35, -100)
t.pendown()

# Draw the right leg
t.right(90)
t.forward(50)

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
