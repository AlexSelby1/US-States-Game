from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

screen.exitonclick()