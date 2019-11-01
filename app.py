import tkinter as tk
from tkinter import filedialog, Text
import os

# Functions


def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    video.append(filename)
    print(filename)


    # Video array
video = []

# Root to tkinter
root = tk.Tk()
root.title("Video to GIF")


# Canvas
canvas = tk.Canvas(root, height=400, width=350, bg="#232323")
canvas.pack()

# Frame
frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=0.6,  relx=0, rely=0.1)

# Open File Button
openFile = tk.Button(root, text="Select Video", padx=10,
                     pady=5, fg="white", bg="#232323", command=addApp)
openFile.pack()

# Confirm Selection Button
confirmFile = tk.Button(root, text="Convert to GIF", padx=9,
                        pady=5, fg="white", bg="#232323")
confirmFile.pack()

# Main loop
root.mainloop()
