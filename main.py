from tkinter import*
from tkinter import ttk
from tkinter import Label, PhotoImage
import tkinter.messagebox
from PIL import Image,ImageTk
import os
import tkinter
from datetime import datetime
from time import strftime
from developer import Developer
from student import Student
from train import Train
from face_recognition import Face_Recognition 
from attendance import Attendance
from chatbot import Chatbot


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        #Background image

        img=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\Background.png")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.phimg=ImageTk.PhotoImage(img)

        bg_label=Label(self.root, image=self.phimg)
        bg_label.place(x=0,y=0,width=1530,height=790)

        #Title
        title_lbl=Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("Roboto",35,"bold"),fg="black",bg="light grey")
        title_lbl.place(x=0,y=0,width=1530,height=65)

        #===================Time======================================================================
        def time():
              string=strftime("%H:%M:%S %p")
              lbl.config(text=string)
              lbl.after(1000,time)

        lbl=Label(title_lbl,font=("roboto",14,'bold'),background='white',foreground='black')
        lbl.place(x=20,y=8,width=115,height=45)
        time()

        #=============================Student button==========================================================================================
        img1=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\graduated.png")
        img1=img1.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg1=ImageTk.PhotoImage(img1)

        B1=Button(root,image=self.phimg1,command=self.student_details,cursor="hand2")
        B1.place(x=200,y=100,width=220,height=220)

        B_1=Button(root,text="Student Details",command=self.student_details, cursor="hand2",font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_1.place(x=200,y=300,width=220,height=40)

        #=============================Face detection button=================================================================================
        img2=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\facescan.png")
        img2=img2.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg2=ImageTk.PhotoImage(img2)

        B2=Button(root,image=self.phimg2,cursor="hand2",command=self.face_data)
        B2.place(x=500,y=100,width=220,height=220)

        B_2=Button(root,text="Face Detector", cursor="hand2",command=self.face_data,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_2.place(x=500,y=300,width=220,height=40)


        #==========================Attendance button========================================================================================
        img3=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\attendance1.png")
        img3=img3.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg3=ImageTk.PhotoImage(img3)

        B3=Button(root,image=self.phimg3,cursor="hand2",command=self.attendance_data)
        B3.place(x=800,y=100,width=220,height=220)

        B_3=Button(root,text="Attendance", cursor="hand2",command=self.attendance_data,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_3.place(x=800,y=300,width=220,height=40)


        #===========================Chat Bot button=========================================================================================
        img4=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\robot.png")
        img4=img4.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg4=ImageTk.PhotoImage(img4)

        B4=Button(root,image=self.phimg4,cursor="hand2",command=self.chatbot)
        B4.place(x=1100,y=100,width=220,height=220)

        B_4=Button(root,text="Chat Bot", cursor="hand2",command=self.chatbot,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_4.place(x=1100,y=300,width=220,height=40)


        #====================Train Data button============================================================================================
        img5=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\train1.png")
        img5=img5.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg5=ImageTk.PhotoImage(img5)

        B5=Button(root,image=self.phimg5,cursor="hand2",command=self.train_data)
        B5.place(x=200,y=380,width=220,height=220)

        B_5=Button(root,text="Train Data", cursor="hand2",command=self.train_data,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_5.place(x=200,y=580,width=220,height=40)

        #===============================Photos button===============================================================
        img6=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\gallery.png")
        img6=img6.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg6=ImageTk.PhotoImage(img6)

        B6=Button(root,image=self.phimg6,cursor="hand2",command=self.open_img)
        B6.place(x=500,y=380,width=220,height=220)

        B_6=Button(root,text="Photos", cursor="hand2",command=self.open_img,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_6.place(x=500,y=580,width=220,height=40)

        #================================Help Desk button=========================================================
        img7=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\coding2.png")
        img7=img7.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg7=ImageTk.PhotoImage(img7)

        B7=Button(root,image=self.phimg7,cursor="hand2",command=self.help)
        B7.place(x=800,y=380,width=220,height=220)

        B_7=Button(root,text="HELP DESK", cursor="hand2",command=self.help,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_7.place(x=800,y=580,width=220,height=40)

        #====================================Exit button=======================================================
        img8=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\exit.png")
        img8=img8.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg8=ImageTk.PhotoImage(img8)

        B8=Button(root,image=self.phimg8,cursor="hand2",command=self.iExit)
        B8.place(x=1100,y=380,width=220,height=220)

        B_8=Button(root,text="Exit", cursor="hand2",command=self.iExit,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_8.place(x=1100,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
            self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
            if self.iExit>0:
                self.root.destroy()
            else:
                return

    #============================Function Buttons=======================================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)

    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

    def chatbot(self):
          self.new_window=Toplevel(self.root)
          self.app=Chatbot(self.new_window)

    def help(self):
          self.new_window=Toplevel(self.root)
          self.app=Developer(self.new_window)

    

        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()