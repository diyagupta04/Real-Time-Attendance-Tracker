from tkinter import*
from tkinter import ttk
from tkinter import Label, PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        #text variables
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        #Background image
        img=Image.open(r"Images\Background.png")
        img = img.resize((1530, 790), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg=ImageTk.PhotoImage(img)

        bg_label=Label(self.root, image=self.phimg)
        bg_label.place(x=0,y=0,width=1530,height=790)  

        #Title
        title_lbl=Label(self.root, text="ATTENDANCE RECORDS", font=("roboto",35,"bold"),bg="hot pink",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=65)

        #MAIN FRAME
        main_frame=Frame(root,bd=2,bg="white")
        main_frame.place(x=15,y=65,width=1500,height=700)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details", font=("roboto", 12, "bold"))
        Left_frame.place(x=35, y=15, width=680, height=650)

        img_left=Image.open(r"Images\bg.jpg")
        img_left = img_left.resize((1530, 790), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg_left=ImageTk.PhotoImage(img_left)

        f_label=Label(Left_frame, image=self.phimg_left)
        f_label.place(x=10,y=0,width=660,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=667,height=485)

        #Label and entry

        #attendance ID
        attendance_label=Label(left_inside_frame,text="Attendance ID:", font=("roboto", 12, "bold"),bg="white")
        attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendance_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_id,font=("roboto", 12, "bold"))
        attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #name
        name_label=Label(left_inside_frame,text="Name:", font=("roboto", 12, "bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("roboto", 12, "bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_label=Label(left_inside_frame,text="Roll No:", font=("roboto", 12, "bold"),bg="white")
        roll_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_roll,font=("roboto", 12, "bold"))
        roll_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #department
        dep_label=Label(left_inside_frame,text="Department:", font=("roboto", 12, "bold"),bg="white")
        dep_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_dep,font=("roboto", 12, "bold"))
        dep_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="Time:", font=("roboto", 12, "bold"),bg="white")
        time_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("roboto", 12, "bold"))
        time_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date:", font=("roboto", 12, "bold"),bg="white")
        date_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("roboto", 12, "bold"))
        date_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)

        #attendance
        attendancelabel=Label(left_inside_frame,text="Attendance Status:", font=("roboto", 12, "bold"),bg="white")
        attendancelabel.grid(row=6,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance, font=("roboto", 12, "bold"),state="readonly",width=18)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=6,column=1,padx=10,pady=4,sticky=W)


        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=16,y=435,width=634,height=35)

        #save button
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("roboto",12,"bold"),bg="hotpink",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=20,font=("roboto",12,"bold"),bg="hotpink",fg="white")
        update_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("roboto",12,"bold"),bg="hotpink",fg="white")
        reset_btn.grid(row=0,column=2)



        #Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details", font=("roboto", 12, "bold"))
        Right_frame.place(x=750, y=15, width=680, height=650)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE, bg="white")
        table_frame.place(x=5,y=5,width=660,height=615)

        #scroll bar and table

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #fetch data

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fin,mode="w",newline="")as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your Data Is Exported To "+os.path.basename(fin)+" Successfully")
        except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}")            

    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_attend_id.set(rows[0])
         self.var_attend_roll.set(rows[1])
         self.var_attend_name.set(rows[2])
         self.var_attend_dep.set(rows[3])
         self.var_attend_time.set(rows[4])
         self.var_attend_date.set(rows[5])
         self.var_attend_attendance.set(rows[6])

    def reset_data(self):
         self.var_attend_id.set("")
         self.var_attend_roll.set("")
         self.var_attend_name.set("")
         self.var_attend_dep.set("")
         self.var_attend_time.set("")
         self.var_attend_date.set("")
         self.var_attend_attendance.set("")


if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()