import tkinter as tk
from time import strftime

clock = tk.Tk()

clock.title("     **** Digital Clock ****")
clock.geometry("500x350")
clock.config(bg="grey")

def time():
    str = strftime("%H:%M:%S %p \n %D")
    label.config(text=str)
    label.after(1000, time)


label = tk.Label(clock, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.place(relx=0.5, rely=0.5,anchor='center')


time()
clock.mainloop()