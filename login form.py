from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x750+0+0")

        ##############Images
        self.bgicon=PhotoImage(file="C:/Users/Ashish Yadav/Pictures/screenshot.PNG")
        self.icon=PhotoImage(file="C:/Users/Ashish Yadav/Documents/rohi/1.png.png")
        #############variable
        self.uname=StringVar()
        self.pas=StringVar()
        bgiconlabel=Label(self.root,image=self.bgicon).pack()
        title=Label(self.root,text="Login System",font="lucide 25 bold",bg='yellow',bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        #############Frame
        Login_frame=Frame(self.root,bg="white")
        Login_frame.place(x=350,y=75)
        Icon_label=Label(Login_frame,image=self.icon,bd=0)
        Icon_label.grid(row=0,columnspan=2)
        Usrname_label=Label(Login_frame,text='UserName',font="lucide 15 bold")
        Usrname_label.grid(row=1,column=0,pady=10,padx=10)
        Usrtext_Entry=Entry(Login_frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        Password_label = Label(Login_frame, text='Password', font="lucide 15 bold")
        Password_label.grid(row=2, column=0, pady=10, padx=10)
        Passtext_Entry = Entry(Login_frame, bd=5,textvariable=self.pas,relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)
        btnlog = Button(Login_frame, text='Login',width=11,command=self.login,font="lucide 15 bold",bg='yellow').grid(row=3,column=1,pady=10)

    def login(self):
        if self.uname.get()=="" or self.pas.get()=="":
            messagebox.showerror("Error",'All fields are required')
        elif self.uname.get()=="Roshni" and self.pas.get()=='rohi@0930':
            messagebox.showerror("Successfull",f"welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error",'Invalid Entry')




root=Tk()
obj=Login_System(root)
root.mainloop()

