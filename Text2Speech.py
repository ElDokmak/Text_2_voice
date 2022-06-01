from tkinter import *
from tkinter import font
import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty("rate")
engine.setProperty("rate", 130)

# creating gui
window = Tk()
window.geometry('400x320')
window.resizable(0, 0)
window.config(bg='black')
window.title("Text To Voice")


Label(window, text="TEXT TO SPEECH", font="arial 20 bold", bg="white").pack()
Label(window, text="Python", font="arial 14 bold",
      bg="darkgreen").pack(side="bottom")
Label(window, text="Enter Text",
      font="arial 16 bold", bg="white").place(x=15, y=60)
Label(window, text="Enter Gender", font="arial 16 bold",
      bg="white").place(x=15, y=130)

# text varaible
Msg = StringVar()
# entry
Entry_field = Entry(window, textvariable=Msg, width='48')
Entry_field.place(x=15, y=100)

# define functions


def text_to_speech():
    Message = Entry_field.get()
    engine.say(Message)
    engine.save_to_file(Message, "python.mp3")
    engine.runAndWait()


def exit():
    window.destroy()


def reset():
    Msg.set("")


def female():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


def male():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


# buttons
Button(window, text="Male", font="arial 16 bold",
       bg="grey", command=male).place(x=25, y=165)

Button(window, text="Female", font="arial 16 bold",
       bg="pink", command=female).place(x=91, y=165)

Button(window, text="PLAY", font="arial 16 bold",
       command=text_to_speech, bg="blue").place(x=25, y=210)

Button(window, text="EXIT", font="arial 16 bold",
       command=exit, bg="red").place(x=100, y=210)

Button(window, text="RESET", font="arial 16 bold",
       command=reset, bg="yellow").place(x=165, y=210)

window.mainloop()
