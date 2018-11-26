
"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Zichen Tan.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################



########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
#######################################################################
import math
import turtle as tt
import rosegraphics as rg
tt.setup(1000 , 1000 , 100 , 50)
window = rg.TurtleWindow()
allen= rg.SimpleTurtle('triangle')
allen.pen = rg.Pen('light blue', 5)
allen.speed = 8
x=40
for o in range(6):
    for i in range(5):
        allen.forward(x)
        allen.right(144)
        x=x+40


zichen = rg.SimpleTurtle('circle')
zichen.pen_up()
zichen.backward(200)
zichen.pen_down()
zichen.pen = rg.Pen('black',20)
zichen.speed = 8
zichen.left(90)
zichen.forward(100)
tt.penup()
tt.bk(200)
tt.pendown()
tt.penup()
tt.pensize(20)
tt.pencolor('red')
tt.left(90)
tt.fd(100)
tt.pendown()
tt.left(90)
tt.circle(30,-180)
tt.right(45)
tt.fd(40*math.sqrt(2))
zichen.right(90)
zichen.pen_up()
zichen.forward(100)
zichen.pen_down()
zichen.right(90)
zichen.forward(100)
zichen.backward(50)
zichen.left(90)
zichen.forward(50)
zichen.left(90)
zichen.pen_up()
zichen.forward(50)
zichen.pen_down()
zichen.backward(100)
zichen.right(90)
zichen.pen_up()
zichen.forward(80)
zichen.left(90)
zichen.forward(100)
zichen.pen_down()
zichen.right(90)
zichen.forward(40)
zichen.backward(20)
zichen.right(90)
zichen.forward(100)
zichen.right(90)
zichen.pen_up()
zichen.forward(20)
zichen.pen_down()
zichen.right(180)
zichen.forward(40)
zichen.pen_up()
zichen.forward(70)
zichen.left(90)
zichen.forward(100)
zichen.right(90)
zichen.pen_down()
zichen.forward(60)
zichen.backward(30)
zichen.right(90)
zichen.forward(100)

tt.penup()
tt.fd(-250)
tt.pendown()
tt.pensize(25)
tt.pencolor("purple")
tt.seth(-40)
for i in range(6):
    tt.circle(40,80)
    tt.circle(-40,80)
tt.circle(40,80/2)
tt.fd(40)
tt.circle(16,180)
tt.fd(40*2/3)

Iris = rg.SimpleTurtle('turtle')
Iris.pen_up()
Iris.backward(50)
Iris.right(90)
Iris.forward(20)
Iris.left(90)
Iris.pen_down()
Iris.pen = rg.Pen('yellow', 10)
Iris.speed = 8
for k in range(6):
    Iris.forward(100)
    Iris.right(60)



window.close_on_mouse_click()




