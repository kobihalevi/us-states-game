import time
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "states_img.gif"
screen.addshape(image)
# Create a turtle and set its shape to the image
map_turtle = turtle.Turtle()
map_turtle.shape(image)
states = pandas.read_csv("states-list.csv")


def write_state(name, x, y):
    """print the country name on the country, accept name, location on the map x + y"""
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x, y)
    writer.color("black")
    writer.write(name, align="center", font=("Arial", 10, "normal"))


def state_info(state_name):
    """Get the state data and return it as separate values"""
    state_data = states[states["state"] == state_name].iloc[0]  # Get the first matching row
    return state_data['state'], state_data['x'], state_data['y']  # Return separate values


def onscreen_message(message):
    """Display a message on the screen for 5 seconds."""
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.color("red")
    writer.goto(0, 0)
    writer.write(message, align="center", font=("Arial", 22, "normal"))
    # Wait for 5 seconds
    time.sleep(3)
    # Clear the message and continue
    writer.clear()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="what's another state's name?").title()
    if answer_state == "Exit":
        onscreen_message("Game Over!")
        break
    if answer_state in states["state"].values and answer_state not in guessed_states:
        state_data, x, y = state_info(answer_state)
        write_state(state_data, x, y)
        guessed_states.append(answer_state)
    else:
        onscreen_message("wrong answer, try again!")

all_states = set(states["state"])
guessed_states_set = set(guessed_states)
missed_states = all_states - guessed_states_set
missed_states_df = pandas.DataFrame(missed_states, columns=["state"])
missed_states_df.to_csv("missed_states.csv", index=False)
# Final Message

if len(guessed_states) == 50:
    onscreen_message("You Won!")
else:
    onscreen_message(f"You missed {len(missed_states)} states!")
    print(missed_states)

screen.exitonclick()
