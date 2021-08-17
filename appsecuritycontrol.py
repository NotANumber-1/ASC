import tkinter as tk
from tkinter import messagebox
import time
result = False
root = tk.Tk()
root.configure(background="black")
root.title("App Security Control")
root.iconbitmap("app.ico")
root.attributes("-toolwindow", True)
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
def prompt():
    global result
    acpmt = messagebox.askyesno(title="App Security Control", message="This app can control your device. Are you sure to run this application? \n\n(You can stop the app from running by clicking [No]. )")
    if acpmt == True:
        messagebox.showinfo(title="ASC - App allowed to run", message="The application will run by clicking [OK]. ")
        result = True
        root.destroy()
    else:
        messagebox.showerror(title="ASC - App blocked by user", message="App has been stopped from running. ")
        result = False
        exit()
accessbtn = tk.Button(text="Access", fg="red", bg="white", font=("Arial", 48), command=prompt)
accessbtn.pack()
accessbtn.place(x=16, y=64)
des = tk.Label(text="Click [Access] to request an access prompt. ", fg="white", font=("Arial", 16), bg="black")
des.pack()
des.place(x=16, y=16)
time.sleep(0.5)
root.mainloop()