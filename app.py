import tkinter as tk
from tkinter import filedialog, Text
import os

# Root to tkinter
root = tk.Tk()
root.title("Video to GIF")
root.resizable(0, 0)


# Canvas
canvas = tk.Canvas(root, height=450, width=350, bg="#232323")
canvas.pack()

# Frame
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Button
openFile = tk.Button(root, text="Select Video", padx=10,
                     pady=5, fg="white", bg="#232323")
openFile.pack()

# Main loop
root.mainloop()
