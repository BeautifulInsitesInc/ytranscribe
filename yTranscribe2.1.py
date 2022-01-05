from transcribe import *
import tkinter as tk
from tkinter import *

root = Tk() # Root window title and dimension
root.title("yTranscript")
root.geometry('1400x1200')

# --- FUNCTION FOR BUTTON ACTION
def clickedsubmit():
    #lbl.configure(text="Submitted")
    #Processed = yTranscribe(SampleInput)
    Sample = (SampleInput.get("1.0",END))  # Assign conents of ImportBox to Sample

    Processed = yTranscribe(Sample)
    print(Sample)
    print(Processed)
    print(url)
    ProcessedOutput.insert(tk.END, Processed)

# -- FUNCTION CLEAR BUTTON
def clickedclear():
    SampleInput.delete('1.0', END)
    ProcessedOutput.delete('1.0', END)
    InputURL.delete(0, END)

# FUNCTIONS END -------------------------------------------------------------------
  
# --- LABEL
lbl = Label(root, text="YouTube Transcriber") # Adding a lable to the root window
lbl.grid(column = 1, row =0) #position on screen

# --- URL ENTRY BOX
InputURL = Entry(root, width = 30)
InputURL.grid(column = 1, row =2)

# --- INPUT BOX
#SampleInput = Text(root)
SampleInput = tk.Text(root, height = 40, width = 80)
SampleInput.grid(column = 1, row = 4)

# -- OUTPUT BOX
ProcessedOutput = tk.Text(root, height = 40, width = 80)
ProcessedOutput.grid(column = 2, row = 4)

# --- SUBMIT BUTTON
btn = Button(root, text="Submit", fg = "red", command=clickedsubmit)
btn.grid(column = 1, row = 1)

# --- CELAR BUTTON
clear = Button(root, text="Clear", fg = "black", command=clickedclear)
clear.grid(column =2, row = 1)



root.mainloop()




