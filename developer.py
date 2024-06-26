from tkinter import*
from tkinter import ttk
from tkinter import Label, PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        #Title
        title_lbl=Label(self.root, text="HELP DESK", font=("Roboto",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=65)

        img_top=Image.open(r"Images\wd.jpg")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root, image=self.phimg_top)
        f_label.place(x=0,y=65,width=1530,height=725)

        #=========Description Frame=========================================
        main_frame=Frame(f_label,bd=2,bg="white")
        main_frame.place(x=1000,y=11,width=500,height=345)

        #===============Description=============================================
        dev_label=Label(main_frame,text='Welcome to our Real-Time Attendance\nTracker project! Leveraging cutting-edge\nmachine learning technology, our system\noffers seamless facial recognition, chatbot\nassistance, and comprehensive attendance\nand student records management.\nExperience efficiency like never before\nwith features designed to streamline\nattendance tracking and enhance\nadministrative tasks. Join us in\nrevolutionizing attendance management!', font=("roboto", 18, "bold"),bg="white",justify="center")
        dev_label.place(x=0,y=5)

        #=====================Image Frame======================================
        leftimg_frame=Frame(f_label,bd=2,bg="white")
        leftimg_frame.place(x=20,y=20,width=200,height=200)

        img_1=Image.open(r"Images\d.jpg")
        img_1 = img_1.resize((196, 196), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg_1=ImageTk.PhotoImage(img_1)

        g_label=Label(leftimg_frame, image=self.phimg_1)
        g_label.place(x=0,y=0,width=196,height=196)

        name_frame=Frame(f_label,bd=2,bg="white")
        name_frame.place(x=250,y=100,width=308,height=80)

        dev_label=Label(name_frame,text='DIYA GUPTA\n', font=("roboto",20, "bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(name_frame,text='[Developer of this project]', font=("roboto", 18, "bold"),bg="white")
        dev_label.place(x=0,y=40)

        #=========Contact Box===========================================
        contact_frame=Frame(f_label,bd=2,bg="white")
        contact_frame.place(x=20,y=300,width=400,height=190)

        contact_label=Label(contact_frame,text='NEED ASSISTANCE?\n', font=("roboto",20, "bold"),bg="white",justify="left")
        contact_label.place(x=0,y=5,height=60)

        img_l=Image.open(r"Images\linkedin.png")
        img_l = img_l.resize((30, 30), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg_l=ImageTk.PhotoImage(img_l)

        h_label=Label(contact_frame, image=self.phimg_l)
        h_label.place(x=10,y=68,width=30,height=30)

        contact_label=Label(contact_frame,text=': linkedin.com/in/diya-gupta-8806272', font=("roboto", 15, "bold"),bg="white")
        contact_label.place(x=50,y=68)

        img_g=Image.open(r"Images\gmail.png")
        img_g = img_g.resize((30, 30), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg_g=ImageTk.PhotoImage(img_g)

        h_label=Label(contact_frame, image=self.phimg_g)
        h_label.place(x=10,y=128,width=30,height=30)

        contact_label=Label(contact_frame,text=': diyagupta17x@gmail.com', font=("roboto", 15, "bold"),bg="white")
        contact_label.place(x=50,y=128)







if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()