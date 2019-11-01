import imageio
import tkinter as tk
from tkinter import filedialog, Text
import os

# init tkinter
root = tk.Tk()
root.geometry('300x250')
root.sourceFile = ''
root.title("Video to GIF")
root.resizable(0, 0)


def chooseFile():
    root.sourceFile = filedialog.askopenfilename(
        parent=root, initialdir="/", title="Select File", filetypes=(("MP4", "*.mp4"), ("All files", "*")))


# Button component for chooseFile()
b_chooseFile = tk.Button(root, text="Select File",
                         width=35, height=2, command=chooseFile)
b_chooseFile.place(x=25, y=75)
b_chooseFile.width = 100

print(root.sourceFile)


# Converting video(images) to .gif
def convertFile(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting {inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frames {frames}')
    print('DONE!')
    writer.close()


# Print location of selected File
def convert():
    convertFile(root.sourceFile, '.gif')


b_convertFile = tk.Button(root, text="Convert", width=15,
                          height=2, command=convert)
b_convertFile.place(x=100, y=125)
b_convertFile.width = 100


# Main Loop
root.mainloop()
