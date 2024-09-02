###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
from turtle import Screen

import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
import turtle as t

import random

from turtle import Screen
t.colormode(255)

color_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
              (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
              (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
              (168, 99, 102)]

def draw_dot():
    t.dot(20,random.choice(color_list))
    t.penup()
    t.forward(50)
def make_a_left_turn():
    t.seth(90)
    draw_dot()
    t.seth(180)
def make_a_right_turn():
    t.seth(90)
    draw_dot()
    t.right(90)
def test():
    for i in range (10):
        draw_dot()
    make_a_left_turn()
    for i in range (10):
        draw_dot()
    make_a_right_turn()

for i in range (5):
    test()




screen = Screen()
screen.exitonclick()
