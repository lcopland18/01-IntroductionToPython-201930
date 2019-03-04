"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Lauren Copland.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
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
########################################################################

import rosegraphics as rg
susan = rg.SimpleTurtle('turtle')
susan.pen = rg.Pen('red',20)
susan.speed = 20
susansize = 150

alex = rg.SimpleTurtle('turtle')
alex.pen = rg.Pen('orange',10)
alex.speed = 10
alexsize = 100

#susan.draw_regular_polygon(6, 100)

#susan.forward(100)
#alex.right(180)
#alex.forward(100)

for k in range(10):
    susan.draw_regular_polygon(6, susansize)
    susan.pen_up()
    susan.right(90)
    susan.forward(20)
    susan.pen_down()
    susansize = susansize-10

for k in range(4):
    alex.draw_square(alexsize)
    alex.pen_up()
    alex.left(90)
    alex.forward(100)
    alex.pen_down()
