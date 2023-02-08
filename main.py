from tkinter import *
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
Timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global Timer,reps
    winsound.MessageBeep ()
    window.after_cancel(Timer)
    label.config(text="TIMER")
    canvas.itemconfig(timer,text="00:00")
    checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    winsound.Beep (440, 1400)
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        label.config (text="BREAK",fg=RED)
        count_down (count=long_break_sec)

    elif reps % 2 ==0:
        label.config (text="BREAK",fg=PINK)
        count_down (count=short_break_sec)

    else :
        label.config (text="WORK")
        count_down (count=work_sec)


    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global Timer
    count_min = math.floor (count / 60)
    count_secs = (count % 60)
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    if count > 0:
      Timer = window.after (1000, count_down, count - 1)
    else:
        start_timer()

        # Creating the checkmark

        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark = "✔"
            checkmark.config(text=mark, fg=GREEN, bg=YELLOW, font=(15))
            checkmark.grid (column=2, row=4)


    canvas.itemconfig (timer, text=f"{count_min}:{count_secs}")


# ---------------------------- UI SETUP ------------------------------- #

# Creating the window

window = Tk ()
window.title ("Pomodoro")
window.config (padx=100, pady=50, bg=YELLOW)

# Creating the canvas

canvas = Canvas (width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage (file="tomato.png")
canvas.create_image (100, 112, image=tomato_img)
timer = canvas.create_text (100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid (column=2, row=2)

# Creating the top label

label = Label (text="TIMER", font=(FONT_NAME, 35, "italic"), fg=GREEN, bg=YELLOW)
label.grid (column=2, row=1)

# Creating the buttons

button_start = Button (text="start", highlightthickness=0, command=start_timer)
button_start.grid (column=1, row=3)

button_reset = Button (text="reset", highlightthickness=0, command=reset)
button_reset.grid (column=3, row=3)

# Creating the checkmark
checkmark = Label (text="", fg=GREEN, bg=YELLOW, font=(15), )



window.mainloop ()
