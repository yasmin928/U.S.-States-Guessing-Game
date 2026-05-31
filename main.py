import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
gusses_states = []

while len(gusses_states) < 50:
    answer_state = screen.textinput(title=f"{len(gusses_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []

        for state in all_states:
            if state not in gusses_states:
                missing_states.append(state)

        # Write missing states on the map in RED
        for state in missing_states:
            state_data = data[data.state == state]

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()

            t.goto(int(state_data.x.item()), int(state_data.y.item()))
            t.color("red")  
            t.write(state)

        break

    if answer_state in all_states and answer_state not in gusses_states:
        gusses_states.append(answer_state)
        state_data = data[data.state == answer_state]
        print(state_data)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(state_data.state.item())


   
