from tkinter import *
from tkinter import ttk
from tkinter import font
import sqlite3
from patient_info import Patient_info
from patient_med_rec import Patient_rec
# from patient_bill import Billing_window
from room_allocation import Room
# from appointment import Appointment
from PIL import ImageTk, Image



conn=sqlite3.connect("HMSDB.db")


class Menu2:
    def __init__(self,master):
        self.master = master
        self.master.title("Healthcare Management System")
        self.master.geometry("2600x1500")
        self.master.config(bg='white')
        self.frame = Frame(self.master)
        self.frame.pack(fill=BOTH, expand=1)

        self.my_canvas = Canvas(self.frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1, )

        self.my_scrollbar = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))

        self.second_frame= Frame(self.my_canvas)
        self.second_frame.config(bg='white')
        self.my_canvas.create_window((0,0),window=self.second_frame,anchor='nw')
        
        self.lbl = Label(self.second_frame,text='MAIN MENU',font='Helvetica 40 bold',fg='blue',bg='white')
        self.lbl.pack()

        self.Inner_frame = Frame(self.second_frame,width=700,height=10,relief='ridge',bg='sky blue',bd=5)
        self.Inner_frame.pack(pady=70)
        self.Inner_frame2 = Frame(self.second_frame,width=700,height=100,relief='ridge',bg='white')
        self.Inner_frame2.pack()
        # self.Inner_frame3 = Frame(self.second_frame,width=700,height=100,relief='ridge',bg='white')
        # self.Inner_frame3.pack(pady=80)
        self.Inner_frame4 = Frame(self.second_frame,width=700,height=100,relief='ridge',bg='white')
        self.Inner_frame4.pack(pady=80)

        self.but1 = Button(self.Inner_frame,text='PATIENT INFORMATION',font='Helvetica 15 bold',fg='red',bg='sky blue',width=26,command=self.patient_info)
        self.but1.grid(row=0,column=0)
        self.but2 = Button(self.Inner_frame,text='PATIENT MEDICAL RECORDS',font='Helvetica 15 bold',fg='red',bg='sky blue',width=26,command=self.patient_med_recs)
        self.but2.grid(row=0,column=1)
        self.but3 = Button(self.Inner_frame,text='ROOM ALLOCATION',font='Helvetica 15 bold',fg='red',bg='sky blue',width=26,command=self.room_allo)
        self.but3.grid(row=0,column=2)
        # self.but4 = Button(self.Inner_frame,text='APPOINTMENTS',font='Helvetica 15 bold',fg='red',bg='sky blue',width=26,command=self.appointments)
        # self.but4.grid(row=0,column=2)
        # self.but5 = Button(self.Inner_frame,text='PATIENT BILL',font='Helvetica 10 bold',fg='red',bg='sky blue',width=25,command=self.patient_bills)
        # self.but5.grid(row=0,column=4)
        self.but6 = Button(self.Inner_frame,text='EXIT',font='Helvetica 15 bold',fg='red',bg='sky blue',width=26,command= self.exit)
        self.but6.grid(row=0,column=3)

        image1 = Image.open("static/People-Patient-Male-icon2.png")
        test = ImageTk.PhotoImage(image1)
        img_lbl = Label(self.Inner_frame2,image = test)
        img_lbl.image = test
        img_lbl.grid(row=0,column=0)
        self.but7 = Button(self.Inner_frame2,text='PATIENT INFORMATION',font='Helvetica 10 bold',fg='sky blue',bg='red',width=25,command=self.patient_info)
        self.but7.grid(row=1,column=0)

        image2 = Image.open("static/record-book-pen-128741502.jpg")
        test2 = ImageTk.PhotoImage(image2)
        img_lbl2 = Label(self.Inner_frame2,image = test2)
        img_lbl2.image = test2
        img_lbl2.grid(row=0,column=1)
        self.but8 = Button(self.Inner_frame2,text='PATIENT MEDICAL RECORDS',font='Helvetica 10 bold',fg='sky blue',bg='red',width=25,command=self.patient_med_recs)
        self.but8.grid(row=1,column=1)

        # image3 = Image.open("clipboard-hi2.png")
        # test3 = ImageTk.PhotoImage(image3)
        # img_lbl3 = Label(self.Inner_frame3,image = test3)
        # img_lbl3.image = test3
        # img_lbl3.grid(row=0,column=0,columnspan=2)
        # self.but9 = Button(self.Inner_frame3,text='APPOINTMENTS',font='Helvetica 10 bold',fg='sky blue',bg='red',width=25,command=self.appointments)
        # self.but9.grid(row=1,column=0,columnspan=2)

        # image4 = Image.open("istockphoto-1279341226-612x6122.jpg")
        # test4 = ImageTk.PhotoImage(image4)
        # img_lbl4 = Label(self.Inner_frame3,image = test4)
        # img_lbl4.image = test4
        # img_lbl4.grid(row=0,column=1)
        # self.but10 = Button(self.Inner_frame3,text='PATIENT BILL',font='Helvetica 10 bold',fg='sky blue',bg='red',width=25,command=self.patient_bills)
        # self.but10.grid(row=1,column=1)

        image5 = Image.open("static/download2.jpg")
        test5 = ImageTk.PhotoImage(image5)
        img_lbl5 = Label(self.Inner_frame4,image = test5)
        img_lbl5.image = test5
        img_lbl5.grid(row=0,column=0,columnspan=2)
        self.but11 = Button(self.Inner_frame4,text='ROOM ALLOCATION',font='Helvetica 10 bold',fg='sky blue',bg='red',width=25,command=self.room_allo)
        self.but11.grid(row=1,column=0,columnspan=2)

        
    def patient_info(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient_info(self.newWindow)
    def patient_med_recs(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient_rec(self.newWindow)
    def room_allo(self):
        self.newWindow = Toplevel(self.master)
        self.app = Room(self.newWindow)
    # def appointments(self):
    #     self.newWindow = Toplevel(self.master)
    #     self.app = Appointment(self.newWindow)
    # def patient_bills(self):
    #     self.newWindow = Toplevel(self.master)
    #     self.app = Billing_window(self.newWindow)
    def exit(self):
        self.master.destroy()