BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas
#READ DATA
data2={}
try:
    data=pandas.read_csv("./data/french_words.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("./data/french_words.csv")
    data2=data.to_dict(orient="records")
else:
    data2=data.to_dict(orient="records")



#UI SETUP

window=Tk()
window.title("FLASH CARD GAME")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

current_card={}


canvas=Canvas(width=800,height=526)
img1=PhotoImage(file="./images/card_front.png")
card_front=canvas.create_image(400, 263, image=img1)
img4=PhotoImage(file="./images/card_back.png")
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
text1=canvas.create_text(400, 150, text=f"", font=("Arial", 40, "italic"))
text2=canvas.create_text(400, 263, text=f"", font=("Arial", 50, "bold"))
def flip_card():
    canvas.itemconfig(text1, text="English",fill='white')
    canvas.itemconfig(text2, text=f"{current_card['English']}",fill='white')
    canvas.itemconfig(card_front,image=img4,)

def new_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(data2)
    canvas.itemconfig(text1,text="French",fill='black')
    canvas.itemconfig(text2,text=f"{current_card['French']}",fill='black')
    canvas.itemconfig(card_front,image=img1)
    flip_timer=window.after(3000,func=flip_card)
def is_known():
    data2.remove(current_card)
    dataa=pandas.DataFrame(data2)
    dataa.to_csv("./data/words_to_learn.csv",index=False)
    new_word()

flip_timer=window.after(3000,func=flip_card)
new_word()
img2=PhotoImage(file="./images/right.png")
button1=Button(image=img2,highlightthickness=0,width=50,height=50,command=is_known)
button1.grid(row=1,column=1)

img3=PhotoImage(file="./images/wrong.png")
button2=Button(image=img3,highlightthickness=0,width=50,height=50,command=new_word)
button2.grid(row=1,column=0)



window.mainloop()
