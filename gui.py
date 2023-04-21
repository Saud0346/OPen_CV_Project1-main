import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import sys
sys.path.append('C:/Users/sauds/Desktop/OPen_CV_Project1-main')
from PLOTS import *

def loading_image():
    # Create a new window
    window = tk.Tk()

    # Load the image and create a PhotoImage object
    image = Image.open('C:/Users/sauds/Desktop/OPen_CV_Project1-main/loading.jpg')
    photo = ImageTk.PhotoImage(image)

    # Create a label widget and set its image attribute to the PhotoImage object
    label = tk.Label(window, image=photo)

    # Pack the label widget to display it in the window
    label.pack()

    # Start the Tkinter event loop
    window.mainloop()


def menue():
    r = tk.Tk()
    r.title('menue')
    button1 = tk.Button(r, text='Faculty Details', width=25, command=faculty_details)
    button2 = tk.Button(r, text='Batch Details', width=25, command=batch_details)
    button3 = tk.Button(r, text='Students Details', width=25, command=a_student_details)
    button4 = tk.Button(r, text='Cross', width=25, command=r.destroy)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    r.mainloop()
    
    
    
menue()

#loading_image()