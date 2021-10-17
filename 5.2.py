Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
import tkinter.font as TheFont
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
Redlight = LED(25)
yellowlight = LED(16)
greenlight = LED(17)

window = Tk()
variable= IntVar()
window.title("Task 5.2")
window.geometry('300x300')
myFont = TheFont.Font(family = 'Helvetica', size = 16, weight = "bold", slant="italic")

def Exit():
    GPIO.cleanup()
    window.quit()

def led_toggling():
    if variable.get()==1:
        yellowlight.on()
        Redlight.off()
        greenlight.off()
    if variable.get()==2:
        yellowlight.off()
        Redlight.on()
        greenlight.off()
    if variable.get()==3:
        yellowlight.off()
        greenlight.on()
        Redlight.off()

Button1 = Radiobutton(window, text = "yellowlight", font = myFont, variable=variable, value=2, command = led_toggling)
Button1.pack(anchor=W)

Button2 = Radiobutton(window, text = "Redlight", font = myFont, variable=variable, value=1, command = led_toggling)
Button2.pack(anchor=N)

Button3 = Radiobutton(window, text = "greenlight", font = myFont, variable=variable, value=3, command = led_toggling)
Button3.pack(anchor=E)

exit_button = Button (window, text = "Exit", font = myFont, command = Exit, height = 3, width = 6)
exit_button.pack(side = RIGHT)

mainloop()