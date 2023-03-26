#import colorgram
#rgb_colors=[]
#colors = colorgram.extract('hirst.jpg', 16)
#
#for color in (colors):
#    r=color.rgb.r
#    g=color.rgb.g
#    b=color.rgb.b
#    col_taple=(r,g,b)
#    rgb_colors.append(col_taple)
#print(rgb_colors)

import turtle as turtle_module
import random
turtle_module.colormode(255)
ted=turtle_module.Turtle()
painting_res=[(239, 221, 113), (18, 111, 193), (223, 60, 95), (235, 150, 76), (116, 147, 208), (143, 88, 50), (212, 127, 164), (34, 194, 117), (139, 183, 18), (189, 18, 39), (108, 105, 194), (232, 55, 45)]
num_dots=100
ted.speed(10)
ted.pu()
ted.hideturtle()
ted.setheading(225)
ted.fd(300)
ted.setheading(0)
for dot_count in range(1,num_dots+1):
    ted.dot(20,random.choice(painting_res))
    ted.fd(50)
    if dot_count%10==0:
        ted.setheading(90)
        ted.fd(50)
        ted.setheading(180)
        ted.fd(500)
        ted.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()