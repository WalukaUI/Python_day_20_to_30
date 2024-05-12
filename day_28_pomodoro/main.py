import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
window = Tk()
timer = None
counter = 0
completed_sessions = ""
# ---------------------------- TIMER RESET ------------------------------- #
def resetall():
    global counter, completed_sessions
    window.after_cancel(timer)
    counter = 0
    completed_sessions = ""
    head_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count_down():
    global counter
    counter += 1
    if counter % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        head_label.config(text="Break", fg=PINK)
    elif counter % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        head_label.config(text="Break", fg=RED)
    else:
        count_down(WORK_MIN * 60)
        head_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global completed_sessions, counter
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_count_down()
        for _ in range(math.floor(counter/2)):
            completed_sessions += "✓"
        mark.config(text=completed_sessions)

# ---------------------------- UI SETUP ------------------------------- #


window.title("Pomodoro")
window.config(pady=50, padx=100, bg=f"{YELLOW}")

canvas = Canvas(width=200, height=224, bg=f"{YELLOW}", highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130 , text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_count_down)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", highlightthickness=0, command=resetall)
reset_btn.grid(column=2, row=2)

mark = Label(text=completed_sessions, fg=GREEN, bg=YELLOW)
mark.grid(column=1, row=3)
head_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
head_label.grid(column=1, row=0)





window.mainloop()