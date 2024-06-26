from tkinter import*
from tkinter import ttk
from tkinter import Label, PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #Background image

        img=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\Background.png")
        img = img.resize((1530, 790), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg=ImageTk.PhotoImage(img)

        bg_label=Label(self.root, image=self.phimg)
        bg_label.place(x=0,y=0,width=1530,height=790)

        #Title
        title_lbl=Label(root, text="STUDENT RECORDS", font=("roboto",35,"bold"),bg="cornflowerblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=65)

        #MAIN FRAME
        main_frame=Frame(root,bd=2,bg="white")
        main_frame.place(x=15,y=70,width=1500,height=700)

        #Left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("roboto", 12, "bold"))
        Left_frame.place(x=35, y=15, width=680, height=650)

        img_left=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\ribon.png")
        img_left = img_left.resize((1530, 790), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg_left=ImageTk.PhotoImage(img_left)

        f_label=Label(Left_frame, image=self.phimg_left)
        f_label.place(x=10,y=0,width=660,height=130)

        #Current course information

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information", font=("roboto", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=660, height=150)

        #Department label

        dep_label=Label(current_course_frame,text="Department", font=("roboto", 12, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("roboto", 12, "bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CSE","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course label
        course_label=Label(current_course_frame,text="Course", font=("roboto", 12, "bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("roboto", 12, "bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","B.TECH","ME","BE","BCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year label

        year_label=Label(current_course_frame,text="Year", font=("roboto", 12, "bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("roboto", 12, "bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester label

        sem_label=Label(current_course_frame,text="Semester", font=("roboto", 12, "bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("roboto", 12, "bold"),state="readonly",width=20)
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Class student information
        class_stu_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information", font=("times new roman", 12, "bold"))
        class_stu_frame.place(x=5, y=290, width=660, height=330)

        #student ID
        stuid_label=Label(class_stu_frame,text="Student ID:", font=("roboto", 12, "bold"),bg="white")
        stuid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        stuid_entry=ttk.Entry(class_stu_frame,textvariable=self.var_id,width=18,font=("roboto", 12, "bold"))
        stuid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        stuname_label=Label(class_stu_frame,text="Name:", font=("roboto", 12, "bold"),bg="white")
        stuname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        stuname_entry=ttk.Entry(class_stu_frame,textvariable=self.var_name,width=18,font=("roboto", 12, "bold"))
        stuname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Aadhar number
        adharno_label=Label(class_stu_frame,text="Aadhar number:", font=("roboto", 12, "bold"),bg="white")
        adharno_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        adharno_entry=ttk.Entry(class_stu_frame,textvariable=self.var_div,width=18,font=("roboto", 12, "bold"))
        adharno_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll number
        sturoll_label=Label(class_stu_frame,text="Roll No.:", font=("roboto", 12, "bold"),bg="white")
        sturoll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        sturoll_entry=ttk.Entry(class_stu_frame,textvariable=self.var_roll,width=18,font=("roboto", 12, "bold"))
        sturoll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        stugen_label=Label(class_stu_frame,text="Gender:", font=("roboto", 12, "bold"),bg="white")
        stugen_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_gender, font=("roboto", 12, "bold"),state="readonly",width=16)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=4,sticky=W)

        #D.O.B.
        studob_label=Label(class_stu_frame,text="Date of Birth:", font=("roboto", 12, "bold"),bg="white")
        studob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studob_entry=ttk.Entry(class_stu_frame,textvariable=self.var_dob,width=18,font=("roboto", 12, "bold"))
        studob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        stuemail_label=Label(class_stu_frame,text="Email ID:", font=("roboto", 12, "bold"),bg="white")
        stuemail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        stuemail_entry=ttk.Entry(class_stu_frame,textvariable=self.var_email,width=18,font=("roboto", 12, "bold"))
        stuemail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone number
        stuph_label=Label(class_stu_frame,text="Phone no.:", font=("roboto", 12, "bold"),bg="white")
        stuph_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        stuph_entry=ttk.Entry(class_stu_frame,textvariable=self.var_phone,width=18,font=("roboto", 12, "bold"))
        stuph_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        stuad_label=Label(class_stu_frame,text="Address:", font=("roboto", 12, "bold"),bg="white")
        stuad_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        stuad_entry=ttk.Entry(class_stu_frame,textvariable=self.var_address,width=18,font=("roboto", 12, "bold"))
        stuad_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Blood group
        blg_label=Label(class_stu_frame,text="Blood group:", font=("roboto", 12, "bold"),bg="white")
        blg_label.grid(row=4,column=2,padx=10,pady=4,sticky=W)

        blg_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_teacher, font=("roboto", 12, "bold"),state="readonly",width=16)
        blg_combo["values"]=("A+","A-","B+","B-","AB+","AB-","O+","O-")
        blg_combo.current(0)
        blg_combo.grid(row=4,column=3,padx=10,pady=10,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radio1.grid(row=8,column=0)

        radio2=ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radio2.grid(row=8,column=1)

        #buttons frame
        btn_frame=Frame(class_stu_frame,bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=5,y=226,width=645,height=70)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("roboto",12,"bold"),bg="cornflowerblue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("roboto",12,"bold"),bg="cornflowerblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("roboto",12,"bold"),bg="cornflowerblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("roboto",12,"bold"),bg="cornflowerblue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame2=Frame(class_stu_frame,bd=2,relief=RIDGE, bg="white")
        btn_frame2.place(x=5,y=262,width=645,height=38)


        phsample_btn=Button(btn_frame2,text="Take Photo Sample",command=self.generate_dataset,width=63,font=("roboto",12,"bold"),bg="cornflowerblue",fg="white")
        phsample_btn.grid(row=0,column=0)


        #Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("roboto", 12, "bold"))
        Right_frame.place(x=750, y=15, width=680, height=650)

        img_right=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\ribon.png")
        img_right = img_right.resize((1530, 790), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg_right=ImageTk.PhotoImage(img_right)

        f_label=Label(Right_frame, image=self.phimg_right)
        f_label.place(x=10,y=0,width=660,height=130)

        #==============================searching system=================================================================
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Searching System", font=("roboto", 12, "bold"))
        search_frame.place(x=5, y=135, width=665, height=70)

        search_label=Label(search_frame,text="Search By:", font=("roboto", 12, "bold"),bg="grey",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search, font=("roboto", 12, "bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Name","Roll No.","Phone No.","D.O.B")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("roboto", 12, "bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("roboto",12,"bold"),bg="cornflowerblue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=9,font=("roboto",12,"bold"),bg="cornflowerblue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5, y=210, width=665, height=410)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Aadhar No.")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Blood Group")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #Function declaration

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="diyagupta1717$$",database="diyadb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                            
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_id.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()
                                                                                        
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
    

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="diyagupta1717$$",database="diyadb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=" "):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update these student details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="diyagupta1717$$",database="diyadb")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update Student SET Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Aadhar_no=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone_no=%s,Address=%s,Blood_group=%s,PhotoSample=%s where Student_id=%s",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_id.get()         
                                                                                                                                                          ))  
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


    #Delete function

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete the details of this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="diyagupta1717$$",database="diyadb")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


    #Reset function
    def reset_data(self):
        self.var_dep.set("Select Department"),  
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set("A+"),
        self.var_radio1.set("")


    #SEARCHING SYSTEM BUTTON
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("ERROR","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="diyagupta1717$$",database="diyadb")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%' ")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)



    #Take Photo Samples

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="diyagupta1717$$", database="diyadb")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update Student SET Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Aadhar_no=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone_no=%s,Address=%s,Blood_group=%s,PhotoSample=%s where Student_id=%s",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_id.get()==id+1         
                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data
                conn.close()

                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                # Initialize the webcam
                cap = cv2.VideoCapture(0) 
                img_id = 0
                while True:
                    ret, myframe = cap.read()
                    if face_cropped(myframe) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(myframe), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        # Update the filename to include the current user's ID
                        file_name_path = f"data/user.{self.var_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    # Add a small delay between frames (10 milliseconds in this case)
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        # Reset img_id for the next user
                        img_id = 0
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

            


        


        
                    


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()