from transcribe import *
import tkinter as tk
from tkinter import *

root = Tk() # Root window title and dimension
root.title("yTranscript")
root.geometry('1400x1200')

# --- FUNCTION FOR BUTTON ACTION
def clicked():
    #lbl.configure(text="Submitted")
    #Processed = yTranscribe(SampleInput)
    Sample = (SampleInput.get("1.0",END))  # Assign conents of ImportBox to Sample
    Processed = yTranscribe(Sample)
    print(Sample)
    print(Processed)
    ProcessedOutput.insert(tk.END, Processed)


# FUNCTIONS END -------------------------------------------------------------------
  
# --- LABEL
lbl = Label(root, text="YouTube Transcriber") # Adding a lable to the root window
lbl.grid(column = 2, row =1) #position on screen

# --- INPUT BOX
#SampleInput = Text(root)
SampleInput = tk.Text(root, height = 200, width = 80)
SampleInput.grid(column = 1, row = 2)

# --- BUTTON WIDGET
btn = Button(root, text="Submit", fg = "red", command=clicked)
btn.grid(column = 1, row = 1)

# -- OUTPUT BOX
ProcessedOutput = tk.Text(root, height = 200, width = 80)
ProcessedOutput.grid(column = 2, row = 2)

root.mainloop()




