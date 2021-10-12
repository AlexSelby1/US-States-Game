import turtle, pandas

screen = turtle.Screen()

screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


answer_state = screen.textinput(title="Guess the state", prompt="What is another state's name?")

if answer_state in states:
    t = turtle.Turtle()
    t.hideturtle()
    t.pu()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x),int(state_data.y))
    t.write(answer_state)

# Used to get x y coords of an image
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

turtle.exitonclick()

