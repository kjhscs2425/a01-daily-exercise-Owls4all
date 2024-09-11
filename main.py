import turtle
#
#
#begin
t = turtle
t.speed(10)
side = 250
theta = 120
phi = 60
t.forward(side)
t.left(theta)
t.forward(side)
for i in range(3):
    t.left(theta)
    t.forward(2*side)
    t.left(theta)
    t.forward(side)
for i in range(6):
    t.left(phi)
    t.forward(side)
#end
#
#
turtle.exitonclick()