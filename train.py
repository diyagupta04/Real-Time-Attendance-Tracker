from tkinter import*
from tkinter import ttk
from tkinter import Label, PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        #Title
        title_lbl=Label(self.root, text="TRAINING DATA SETS", font=("roboto",35,"bold"),bg="deepskyblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=65)

        img_top=Image.open(r"Images\train.jpg")
        img_top = img_top.resize((1530, 790), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root, image=self.phimg_top)
        f_label.place(x=0,y=65,width=1530,height=790)

        #Button
        B_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier, cursor="hand2",font=("roboto",30,"bold"),bg="deepskyblue",fg="white")
        B_1.place(x=615,y=380,width=300,height=60)


        #Training function

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #Grey scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
                
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #Training classifier and save

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!!", parent=self.root)


       



if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()