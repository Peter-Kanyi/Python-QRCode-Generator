import pyqrcode
import png
from PIL import ImageTk, Image
from pyqrcode import QRCode
import tkinter as tk 
from tkinter import *
import PIL.Image

window = Tk()  
window.geometry('300x350')
window.title('QR Code generator by Kanyi')

Label(window,text='Copy Paste your link to create a QR Code',font='arial 15').pack()
# String which represents the QR code
s = tk.StringVar()
  
# Generate QR code
def create_qrcode():
    s1=s.get()
    qr = pyqrcode.create(s1)
    qr.png('myqr.png', scale = 6)
    Label(window,text='Your QR Code has been created and saved').pack()

Entry(window,textvariable=s,font='arial 15').pack()
Button(window,text='create',bg='green',command=create_qrcode).pack()
window.mainloop()