from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cv2
import os
import imutils
import Part_1 as pt
import Part_3 as pt3


class App:
    
    def __init__(self, window):
        
        def deleteLabel():
            if len(self.name.get()) == 0:
                messagebox.showerror(message = 'Please enter a valid First Name', title = 'Invalid Name')
                return
            else:
                pt.SaveUser(self.name.get())
                self.name.delete(0, END)
                messagebox.showinfo(message = 'Successfully registered user', title = 'Successfully')
            
        self.wind = window
        self.wind.title('Facial Recognition')
        
        #Creating a Frame Container
        frame = LabelFrame(self.wind, text = 'New User Registration')
        frame.grid(column = 0, row = 0, columnspan = 3, pady = 20, padx = 20)
        
        #Name Input
        Label(frame, text = 'Name: ').grid(column=0, row=1, pady=6)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(column = 1, row = 1)
        
        #Button Add User 
        ttk.Button(frame, text = 'Save User', command = lambda: deleteLabel()).grid(row = 2, columnspan = 2,sticky = W + E)
        ttk.Button(frame, text = 'Recognition', command = lambda: pt3.recognition()).grid(row = 3, columnspan = 2,sticky = W + E)
        
        #Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0 , columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Last Name', anchor = CENTER)
        
        
if __name__ == '__main__':
    window = Tk()
    application = App(window)
    window.mainloop()    