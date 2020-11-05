# Billing_Software.py
#import tkinter
#import tkinter as tk
from tkinter import *

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self,root, text="Billing Software", bd=12, relief=GROOVE,bg=bg_color,fg="white", font=("times new roman", 15, "bold"))
        
        ##Customer Detail Frame
    
        F1=LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl=Label(F1, text="Customer Name",bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0,column=0,padx=20, pady=5)
        cname_txt=Entry(F1,width=20,font="arial 15").grid(row=0,column=1,pady=5, padx=10)

root=Tk()
obj = Bill_App(root)
root.mainloop()

