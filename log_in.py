from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import font
import bcrypt
import sqlite3
from PIL import ImageTk, Image
from menu2 import Menu2
from menu import Menu1
from menu3 import Menu3
from signup import Window



def main():
    window =Tk()
    app = MainWindow(window)
    mainloop()

class MainWindow:
    def __init__(self,master):
        self.master = master
        self.master.title("Healthcare Management System")
        self.master.geometry("2600x1500")
        self.frame = Frame(self.master,bg='cadet blue')
        self.frame.pack(fill=BOTH, expand=1)
        self.Username = StringVar()
        self.Password = StringVar()
        self.menu = StringVar()

        self.frame1 = Frame(self.frame,bg='cadet blue',width=800,height=900)
        self.frame1.grid(row=1,column=0)
        self.frame2 = Frame(self.frame,bg='cadet blue',width=800,height=300)
        self.frame2.grid(row=0,column=1)
        self.frame3 = Frame(self.frame,bg='cadet blue',width=600,height=300)
        self.frame3.grid(row=0,column=0)
        self.frame4 = Frame(self.frame,bg='cadet blue',width=800,height=300)
        self.frame4.grid(row=1,column=1,padx=50)

        image1 = Image.open("static/istockphoto-1214423422-612x6122.jpg")
        test = ImageTk.PhotoImage(image1)
        img_lbl = Label(self.frame1,image = test)
        img_lbl.image = test
        img_lbl.grid(row=0,column=0)

        self.lbl1 = Label(self.frame3,text='HEALTHCARE',font="Helvetica 30 bold",bg='cadet blue',fg='red')
        self.lbl1.pack(pady=20)
        self.lbl2 = Label(self.frame3,text='MANAGEMENT',font="Helvetica 30 bold",bg='cadet blue',fg='red')
        self.lbl2.pack()
        self.lbl3 = Label(self.frame3,text='SYSTEM',font="Helvetica 30 bold",bg='cadet blue',fg='red')
        self.lbl3.pack(pady=20)

        self.lbl4 = Label(self.frame2,text="Don't have an account?",font="Helvetica 12 bold",bg='cadet blue')
        self.lbl4.grid(row=0,column=0)
        self.signup_but = Button(self.frame2,text="SIGN UP",font="Helvetica 15 bold",width=10,fg='blue',command=self.signup)
        self.signup_but.grid(row=1,column=0,pady=10)

        # self.Inner_frame1 = Frame(self.frame2,width=800,height=400,relief='ridge',bg='red',bd=10)
        # self.Inner_frame1.grid(row=1,column=1,pady=10)
        self.Inner_frame2 = Frame(self.frame4,width=400,height=200,relief='ridge',bg='cadet blue')
        self.Inner_frame2.grid(row=7,column=0,sticky=W,pady=120)

        self.lbl5 = Label(self.frame4,text="Let's log you in!",font="Helvetica 20 bold",bg='cadet blue',fg='red')
        self.lbl5.grid(row=0,column=0,sticky=W)

        self.lbl_username = Label(self.frame4,text='Username',font="Helvetica 20 bold",bg='cadet blue',bd=22)
        self.lbl_username.grid(row=1,column=0,sticky=W)
        self.entry_username = Entry(self.frame4,font="Helvetica 20 bold",textvariable=self.Username,width=30,bd=2,fg='blue')
        self.entry_username.grid(row=2,column=0)
        self.lbl_password = Label(self.frame4,text='Password',font="Helvetica 20 bold",bg='cadet blue',bd=22)
        self.lbl_password.grid(row=4,column=0,sticky=W)
        self.entry_password = Entry(self.frame4,font="Helvetica 20 bold",textvariable=self.Password,width=30,bd=2,fg='blue',show='*')
        self.entry_password.grid(row=5,column=0)

        self.login_but = Button(self.Inner_frame2,text='Login',font="Helvetica 15",fg='blue',width=10,command= self.Login_system)
        self.login_but.grid(row=0,column=0)
        self.exit_but = Button(self.Inner_frame2,text='Exit',font="Helvetica 15",fg='blue',width=10,command= self.Exit)
        self.exit_but.grid(row=0,column=1)

    def signup(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window(self.newWindow)

    def Login_system(self):
        usernames = (self.Username.get())
        passwords = (self.Password.get())
        conn = sqlite3.connect("HMSDB.db")
        cursor = conn.cursor()
        db_pw = list(cursor.execute('select PASSWORD from LOGIN where USERNAMES=?',(usernames,)))
        if bcrypt.checkpw(passwords.encode('utf8'),db_pw[0][0]):
            user = list(cursor.execute('select * from LOGIN where USERNAMES=?',(usernames,)))
            x = len(user)
            if x!=0:
                db_role = list(cursor.execute('select ROLE from LOGIN where USERNAMES=?',(usernames,)))
                if db_role[0][0]=='Doctor':
                    self.newWindow = Toplevel(self.master)
                    self.app = Menu1(self.newWindow)
                elif db_role[0][0]=='Nurse':
                    self.newWindow = Toplevel(self.master)
                    self.app = Menu2(self.newWindow)
                elif db_role[0][0]=='Receptionist':
                    self.newWindow = Toplevel(self.master)
                    self.app = Menu3(self.newWindow)
                # match db_role[0][0]:
                #     case "Doctor":
                #         self.newWindow = Toplevel(self.master)
                #         self.app = Menu1(self.newWindow)
                #     case "Nurse":
                #         self.newWindow = Toplevel(self.master)
                #         self.app = Menu2(self.newWindow)
                #     case "Receptionist":
                #         self.newWindow = Toplevel(self.master)
                #         self.app = Menu3(self.newWindow)
        else:
            tkinter.messagebox.askretrycancel("HEALTHCARE MANAGEMENT SYSTEM" , "PLEASE ENTER VALID USERNAME AND PASSWORD")

    def Exit(self):
        self.master.destroy()

if __name__ == "__main__":
    main()