from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  


class Chatbot:
    def __init__(self,root):
        self.root=root
        self.root.title("CHATBOT")
        self.root.geometry("730x620+0+0")
        self.root.bind("<Return>",self.enter_func)


        main_frame=Frame(self.root,bd=4,bg="black",width=610)
        main_frame.pack()


        img_chat=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\robot.png")
        img_chat= img_chat.resize((150, 70), Image.BICUBIC)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="CHATBOT",font=('roboto',30,'bold'),fg='white',bg='black')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,bg='dim grey',relief=RAISED,font=('roboto',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg="black",width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type something",font=('roboto',14,'bold'),fg='white',bg='black')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=38,font=('roboto',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('roboto',15,'bold'),width=6,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear",command=self.clear,font=('roboto',15,'bold'),width=6,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=""
        self.label_11=Label(btn_frame,text=self.msg,font=('roboto',14,'bold'),fg='red',bg='black')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)



    #function declaration
        
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set("")

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set("")


    def send(self):
        send="\t\t\t"+"You: "+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)


        if(self.entry.get()==""):
            self.msg="Please provide an input message!"
            self.label_11.config(text=self.msg,fg="red")
        else:
            self.msg=""
            self.label_11.config(text=self.msg,fg="red")

        #Conversation between bot and human
        if(self.entry.get()=="hello" or self.entry.get()=="Hello"):
            self.text.insert(END,'\n\n'+'Bot: Hey! How are you doing?')

        elif(self.entry.get()=="Fine" or self.entry.get()=="fine" or self.entry.get()=="Good" or self.entry.get()=="good"):
            self.text.insert(END,'\n\n'+'Bot: Nice to hear that.')

        elif(self.entry.get()=="who created you?" or self.entry.get()=="Who created you?"):
            self.text.insert(END,'\n\n'+'Bot: Diya created me using Python.')

        elif(self.entry.get()=="what is your name?" or self.entry.get()=="What is your name?" or self.entry.get()=="what's your name?" or self.entry.get()=="What's your name?"):
            self.text.insert(END,'\n\n'+'Bot: My name is Mr. Maddy!')

        elif(self.entry.get()=="bye" or self.entry.get()=="Bye"):
            self.text.insert(END,'\n\n'+'Bot: It was nice talking to you.\nHave a good day!')

        elif(self.entry.get()=="what is machine learning?" or self.entry.get()=="What is machine learning?"):
            self.text.insert(END,'\n\n'+'Bot: Machine learning is a branch\nof artificial intelligence (AI) that\nfocuses on developing algorithms and\nmodels that enable computers to\nlearn and make predictions or decisions\nbased on data, without being explicitly\nprogrammed to do so.')

        elif(self.entry.get()=="how does face recognition work?" or self.entry.get()=="How does face recognition work?"):
            self.text.insert(END,'\n\n'+'Bot: Face recognition works by analyzing\nand comparing key facial features,\nsuch as the distance between the eyes,\nthe shape of the nose, and the\ncontours of the face.')

        elif(self.entry.get()=="how does face recognition work step by step?" or self.entry.get()=="How does face recognition work step by step?"):
            self.text.insert(END,'\n\n'+'Bot: Face recognition includes:\n1.Face Detection\n2.Feature Extraction\n3.Feature Representation\n4.Face Matching/Recognition\n5.Decision Making\n6.Update and Feedback(if applicable)')

        elif(self.entry.get()=="how many countries are using face recognition technology as per now?" or self.entry.get()=="How many countries are using face recognition technology as per now?"):
            self.text.insert(END,'\n\n'+'Bot: 109 countries!')

        elif(self.entry.get()=="What is python programming?" or self.entry.get()=="what is python programming?"):
            self.text.insert(END,'\n\n'+"Bot: Python programming is a\nversatile, high-level\nprogramming language known for\nits simplicity and readability.\nIt's widely used across various\ndomains, including web\ndevelopment, data science,\nartificial intelligence,\nautomation, and scripting.")

        elif(self.entry.get()=="what is chatbot?" or self.entry.get()=="What is chatbot?"):
            self.text.insert(END,'\n\n'+'Bot: A chatbot is a computer\nprogram that conducts a conversation\nwith users via textual or auditory\nmethods, simulating human\ninteraction for various purposes\nsuch as customer service,\ninformation retrieval, or\nentertainment.')

        else:
            self.text.insert(END,'\n\n'+"Bot: Sorry! I didn't get it.")





if __name__=="__main__":
    root=Tk()
    obj=Chatbot(root)
    root.mainloop()