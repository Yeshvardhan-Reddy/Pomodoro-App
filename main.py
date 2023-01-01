from tkinter import *
import math
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    start_btn.config(state='normal')
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    start_btn.config(state='disabled')
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        label_title.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label_title.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        label_title.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        window.iconify()
        window.deiconify()
        start_timer()
        ticks = ""
        sessions = math.floor((reps/2))
        for _ in range(sessions):
            ticks += "✔"
        checkmarks.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

label_title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label_title.config(pady=10)
label_title.grid(column=1, row=0)

start_btn = Button(text="Start", fg=RED, highlightthickness=0, command=start_timer)
start_btn.config(padx=5, pady=1)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", fg=RED, highlightthickness=0, command=reset_timer)
reset_btn.config(padx=5, pady=1)
reset_btn.grid(column=2, row=2)

checkmarks = Label(bg=YELLOW, fg=GREEN, font=("", 18))
checkmarks.grid(column=1, row=3)

window.mainloop()
