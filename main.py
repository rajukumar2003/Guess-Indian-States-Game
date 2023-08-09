import turtle as t
import pandas

screen = t.Screen()

screen.setup(width=800, height=720)
screen.title("Indian States Game")
image = "map-india.gif"
screen.addshape(image)
t.shape(image)

# Creating a dataframe
data = pandas.read_csv("indian_states.csv")

state_list = data.state.tolist()

list_of_states = []

# -------------FUNCTION TO GET COORDINATES ON MAP------------
# def get_click_on_cor(x, y):
#     print(x, y)
# t.onscreenclick(get_click_on_cor)
# t.mainloop()

while len(list_of_states) < 28:
    user_guess = screen.textinput(title=f"{len(list_of_states)}/{len(state_list)}State correct",
                                  prompt="What's another state name").title()

    if user_guess == "Exit":
        break
    if user_guess in state_list:
        list_of_states.append(user_guess)

        x_value = int(data[data.state == user_guess].x.iloc[0])
        y_value = int(data[data.state == user_guess].y.iloc[0])

        new_turtle = t.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x_value, y_value)
        new_turtle.write(arg=f"{user_guess}", align="center", font=('Courier', 10, 'bold'))

        #                   OR
        # state_data = data[data.state == user_guess]
        # new_state.write(state_data.state.item())

states_to_learn_list = []

for i in range(len(state_list) - len(list_of_states)):
    if state_list[i] in list_of_states:
        continue

    else:
        states_to_learn_list.append(state_list[i])


data = pandas.Series(states_to_learn_list)
data.to_csv("States_to_learn.csv")
