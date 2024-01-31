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
reps=0
row=3
timer=None
check_marks=None

def reset_timer():
    global reps
    global check_marks
    window.after_cancel(timer)
    text("Timer",PINK)
    canvas.itemconfig(timer_text,text="00:00")
    check_marks = Label(text="", fg=RED, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
    reps=0


def add_checkmarks():
    global row
    global check_marks
    check_marks = Label(text="$", fg=RED, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
    check_marks.grid(row=row, column=1)
    row+=1
def text(time,color):
    timer = Label(text=time, fg=color, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    timer.grid(row=0, column=1)
#TIMER MEXHANISM
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        count_down(30)
        text("BREAK TIME",GREEN)
        add_checkmarks()



    elif reps%2==0:
        count_down(10)
        text("BREAK TIME",GREEN)
        add_checkmarks()

    else:
        count_down(15)
        text("WORK TIME",RED)
#COUNTDOWN MECHANISM
def count_down(count):
    min=math.floor(count/60)
    sec=count%60
    if sec==0:
        sec="00"
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()



#USER INTERFACE SETUP
window=Tk()
window.title("POMODORE")
window.config(padx=110,pady=70,bg=YELLOW)
text("Timer", PINK)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button=Button(text="start",fg=RED,font=(FONT_NAME,10),highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)
reset_button=Button(text="reset",fg=RED,font=(FONT_NAME,10),highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)
window.mainloop()
