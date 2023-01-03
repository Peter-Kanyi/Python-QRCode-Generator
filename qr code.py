#Let's import the required libraries
import pyqrcode #for generating the QR code
import png
from PIL import ImageTk, Image
from pyqrcode import QRCode
import tkinter as tk #for creating the gui window
from tkinter import *
import PIL.Image
#Next, we create the GUI window
window = Tk()  #creates a GUI window called Window
window.geometry('300x350') #Specifies the size of the window
window.title('QR Code generator by Kanyi') #the title of the window

Label(window,text='Copy Paste your link to create a QR Code',font='arial 15').pack()
# String which represents the QR code
s = tk.StringVar()
  
#QRCode generation function
def create_qrcode():
    s1=s.get()
    qr = pyqrcode.create(s1)
    qr.png('myqr.png', scale = 6)
    Label(window,text='Your QR Code has been created and saved').pack()

    #Button and Entry Field
Entry(window,textvariable=s,font='arial 15').pack()
Button(window,text='create',bg='green',command=create_qrcode).pack()
window.mainloop()
