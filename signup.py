from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import font
import bcrypt
import sqlite3
from PIL import ImageTk, Image


class Window:
    def __init__(self,master):
        self.master = master
        self.master.title("Healthcare Management System")
        self.master.geometry("2600x1500")
        self.frame = Frame(self.master,bg='white')
        self.frame.pack(fill=BOTH, expand=1)
        self.Username = StringVar()
        self.Password = StringVar()
        self.Role = StringVar()
        self.menu = StringVar()
        self.menu.set("Select a role")

        self.frame1 = Frame(self.frame,bg='white',width=800,height=900)
        self.frame1.grid(row=1,column=0)
        self.frame2 = Frame(self.frame,bg='white',width=800,height=220)
        self.frame2.grid(row=0,column=1)
        self.frame3 = Frame(self.frame,bg='white',width=600,height=220)
        self.frame3.grid(row=0,column=0,columnspan=2)
        self.frame4 = Frame(self.frame,bg='white',width=800,height=300)
        self.frame4.grid(row=1,column=1)

        image1 = Image.open("static/Healthcare22.png")
        test = ImageTk.PhotoImage(image1)
        img_lbl = Label(self.frame1,image = test)
        img_lbl.image = test
        img_lbl.grid(row=0,column=0)

        self.lbl1 = Label(self.frame3,text='HEALTHCARE MANAGEMENT SYSTEM',font="Helvetica 30 bold",bg='white',fg='red')
        self.lbl1.pack(pady=10)
        # self.lbl2 = Label(self.frame3,text='MANAGEMENT',font="Helvetica 30 bold",bg='cadet blue',fg='red')
        # self.lbl2.pack()
        # self.lbl3 = Label(self.frame3,text='SYSTEM',font="Helvetica 30 bold",bg='cadet blue',fg='red')
        # self.lbl3.pack(pady=10)

        # self.Inner_frame1 = Frame(self.frame2,width=800,height=400,relief='ridge',bg='red',bd=10)
        # self.Inner_frame1.grid(row=1,column=1,pady=10)
        self.Inner_frame2 = Frame(self.frame4,width=400,height=200,relief='ridge',bg='white')
        self.Inner_frame2.grid(row=7,column=0,sticky=W,pady=20)

        self.lbl5 = Label(self.frame4,text="Sign Up!",font="Helvetica 20 bold",bg='white',fg='red')
        self.lbl5.grid(row=0,column=0,sticky=W)

        self.lbl_username = Label(self.frame4,text='Username',font="Helvetica 20 bold",bg='white',fg='blue',bd=22)
        self.lbl_username.grid(row=1,column=0,sticky=W)
        self.entry_username = Entry(self.frame4,font="Helvetica 20 bold",textvariable=self.Username,width=30,bd=2,fg='red')
        self.entry_username.grid(row=2,column=0)
        self.lbl_password = Label(self.frame4,text='Password',font="Helvetica 20 bold",bg='white',fg='blue',bd=22)
        self.lbl_password.grid(row=3,column=0,sticky=W)
        self.entry_password = Entry(self.frame4,font="Helvetica 20 bold",textvariable=self.Password,width=30,bd=2,fg='red')
        self.entry_password.grid(row=4,column=0)
        # self.lbl_role = Label(self.frame4,text='Role',font="Helvetica 20 bold",bg='white',fg='blue',bd=22)
        # self.lbl_role.grid(row=5,column=0,sticky=W)
        # self.entry_role = Entry(self.frame4,font="Helvetica 20 bold",textvariable=self.Role,width=30,bd=2,fg='red')
        # self.entry_role.grid(row=6,column=0)
        self.drop = OptionMenu(self.frame4,self.menu,"Doctor","Nurse","Receptionist")
        self.drop.grid(row=5,column=0,sticky=W,pady=20)

        self.login_but = Button(self.Inner_frame2,text='SignUp',font="Helvetica 15",fg='blue',width=10,command= self.signup_system)
        self.login_but.grid(row=0,column=0)
        self.exit_but = Button(self.Inner_frame2,text='Exit',font="Helvetica 15",fg='blue',width=10,command= self.Exit)
        self.exit_but.grid(row=0,column=1)

    def signup_system(self):
        conn = sqlite3.connect("HMSDB.db")
        cursor = conn.cursor()
        usernames = (self.Username.get())
        passwords = (self.Password.get())
        roles = (self.menu.get())
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(passwords.encode('utf8'),salt)
        a = list(cursor.execute('select * from LOGIN where USERNAMES = ?',(usernames,)))
        x = len(a)
        if x!=0:
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM","USERNAME ALREADY EXISTS")
        else:
            cursor.execute('insert into LOGIN values(?,?,?)',(usernames,hashed_pw,roles))
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM","SIGN UP COMPLETE")
            conn.commit()

    def Exit(self):
        self.master.destroy()