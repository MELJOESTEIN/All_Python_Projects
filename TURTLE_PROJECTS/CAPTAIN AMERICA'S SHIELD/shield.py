import turtle

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/


t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("Black")
t.shape("circle")
t.goto(-30, -280)
t.color("red")
t.begin_fill()
t.circle(300)
t.end_fill()

t.goto(-30, -240)
t.color("White")
t.begin_fill()
t.circle(260)
t.end_fill()

t.goto(-30, -200)
t.color("red")
t.begin_fill()
t.circle(220)
t.end_fill()

t.goto(-30, -160)
t.color("Blue")
t.begin_fill()
t.circle(180)
t.end_fill()

t.goto(-200, 75)
t.begin_fill()
t.color('white')

for i in range(5):
    t.forward(340)
    t.right(144)
t.end_fill()
t.hideturtle()
turtle.done()
