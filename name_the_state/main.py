import turtle
import pandas
from turtle import Turtle, Screen

screen = turtle.Screen()
screen.title("States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
is_game_on = True
datas = pandas.read_csv("./50_states.csv")
states = datas["state"].to_list()
correct_answers = []



while is_game_on:
    answer_box = screen.textinput(f'State name {len(correct_answers)}/50', "Enter a state").title()
    if answer_box == "Exit":
        missing_states = [state for state in states if state not in correct_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")
        is_game_on = False
    if answer_box in states:
        correct_answers.append(answer_box)
        t = Turtle()
        t.penup()
        t.hideturtle()
        totai = datas[datas["state"] == answer_box]
        t.goto(int(totai["x"]), int(totai["y"]))
        t.write(answer_box)



print(correct_answers)
print(missing_states)






# turtle.mainloop()
# screen.exitonclick()



