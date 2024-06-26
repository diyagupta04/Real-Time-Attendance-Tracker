from tkinter import*
from tkinter import ttk
from tkinter import Label, PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        #Title
        title_lbl=Label(self.root, text="FACE RECOGNITION", font=("roboto",35,"bold"),bg="midnight blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=65)

        img_top=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\fr.jpg")
        img_top = img_top.resize((1530,725), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root, image=self.phimg_top)
        f_label.place(x=0,y=65,width=1530,height=750)


        #Button
        B_1=Button(f_label,text="Face Recognition",command=self.face_recog, cursor="hand2",font=("roboto",18,"bold"),bg="darkgreen",fg="white")
        B_1.place(x=655,y=620,width=220,height=40)


    #ATTENDANCE
    def mark_attendance(self,i,j,m,n):
        with open("diya.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list)and (j not in name_list)and(m not in name_list)and(n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{i},{j},{m},{dtString},{d1},Present")


    #face recognition

    def face_recog(self):
        def draw_b(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            grey_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(grey_image,scaleFactor,minNeighbour)


            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)
                id,predict=clf.predict(grey_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))


                conn=mysql.connector.connect(host="localhost",username="root",password="diyagupta1717$$",database="diyadb")
                my_cursor=conn.cursor()


                my_cursor.execute("Select Name from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("Select Roll_no from student where Student_id="+str(id))
                j=my_cursor.fetchone()
                j="+".join(j)

                my_cursor.execute("Select Department from student where Student_id="+str(id))
                m=my_cursor.fetchone()
                m="+".join(m)

                my_cursor.execute("Select Student_id from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                
                if confidence>77:
                    cv2.putText(img,f"ID: {n}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll: {j}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name: {i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {m}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,j,m,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_b(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
         
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()

        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


            


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()