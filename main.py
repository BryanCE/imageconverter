import os
from PIL import Image, ImageFile, ImageTk
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("Bryan's Image Converter")

# Global variable to store file path
filePath = None

# Function to open file dialog
def openFile():
    global filePath
    filePath = filedialog.askopenfilename(title="Select a .webp file")
    if filePath:
        convertLbl.config(text="File: " + filePath)
    else:
        convertLbl.config(text="Convert to:")

def viewImage(file, mainRoot=root):
    try:
        # Open the image file
        image = Image.open(file)

        # Create a new Tkinter window as a Toplevel of the main window
        viewer_root = tk.Toplevel(mainRoot)
        viewer_root.title("Image Viewer")

        # Create a canvas with the same dimensions as the image
        canvas = tk.Canvas(viewer_root, width=image.width, height=image.height)
        canvas.pack()

        # Convert the PIL Image to a Tkinter-compatible PhotoImage
        photo = ImageTk.PhotoImage(image)

        # Add the PhotoImage to the canvas
        canvas.create_image(0, 0, anchor='nw', image=photo)

        # Keep a reference to the PhotoImage object
        root.photo = photo

        # Run the Tkinter event loop
        root.mainloop()

    except Exception as e:
        convertLbl.config(text="Invalid image file!")
        print(e)
        return

# Function to convert image
def convert(file):
    if wantsJpeg.get() == 0 and wantsPng.get() == 0:
        convertLbl.config(text="Select a format to convert to!")
        return
    if file is None:
        convertLbl.config(text="No file selected!")
        return

    # Get the file extension
    _, ext = os.path.splitext(file)

    # Check if the file is a valid image
    try:
        image = Image.open(file)
    except Exception as e:
        convertLbl.config(text="Invalid image file!")
        return

    # Check if the user wants to convert to png
    if wantsPng.get() == 1:
        png_path = file.replace(ext, ".png")
        image.save(png_path, "PNG")
        convertLbl.config(text="Converted to PNG")
    # Check if the user wants to convert to jpeg
    if wantsJpeg.get() == 1:
        jpg_path = file.replace(ext, ".jpg")
        image.save(jpg_path, "JPEG")
        convertLbl.config(text="Converted to JPEG")
    convertLbl.config(text="Conversion complete")


# Create widgets ----------------------------------------------------------------
openFileBtn = tk.Button(root, text="Choose Image", height=2, width=40, command=openFile)
convertLbl = tk.Label(root, text="Convert to:")
# make a check box for png and jpeg
wantsPng = tk.IntVar()
wantsJpeg = tk.IntVar()
pngCheck = tk.Checkbutton(
    root, text="PNG", variable=wantsPng, onvalue=1, offvalue=0
)
jpegCheck = tk.Checkbutton(
    root, text="JPG/JPEG", variable=wantsJpeg, onvalue=1, offvalue=0
)
convertBtn = tk.Button(root, text="Convert/Save", height=2, width=30,  command=lambda: convert(filePath))
viewBtn = tk.Button(root, text="View", height=2, width=30, command=lambda: viewImage(filePath))
# Create a frame to contain the button
exitBtnFrame = tk.Frame(root)
exitBtn = tk.Button(exitBtnFrame, text="Exit", height=2, width=30, command=root.destroy)
exitBtn.pack(expand=True, fill="both")


# Grid the widgets ----------------------------------------------------------------
openFileBtn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
convertLbl.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
pngCheck.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
jpegCheck.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")
viewBtn.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew") 
convertBtn.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
exitBtnFrame.grid(row=5, column=0, columnspan=2, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)
# root.grid_rowconfigure(3, weight=1)


root.mainloop()