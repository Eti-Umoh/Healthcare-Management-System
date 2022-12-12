from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter.messagebox
import sqlite3
from PIL import ImageTk, Image

class Billing_window:
    def __init__(self,master):
        self.master = master
        self.master.title("Healthcare Management System")
        self.master.geometry("1500x800")
        # self.frame = Frame(self.master)
        # self.frame.pack()

        image1 = Image.open("static/images2.png")
        test = ImageTk.PhotoImage(image1)
        img_lbl = Label(self.master,image = test)
        img_lbl.image = test
        img_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        self.pat_id = IntVar()
        self.room_ch = IntVar()
        self.dat_dchr = StringVar()
        self.treat = StringVar()
        self.treat_cd =StringVar()
        self.treat_cs = IntVar()
        self.med = StringVar()
        self.med_qty = IntVar()
        self.med_prc = IntVar()

        self.mainlbl = Label(self.master, text='PATIENT BILLING WINDOW', font='Helvetica 20 bold',fg='blue',bg='black')
        self.mainlbl.pack(pady=50)

        self.Inner_frame1 = Frame(self.master, width=500, height=250, bg='black', relief='ridge', bd=5)
        self.Inner_frame1.pack()
        self.Inner_frame2 = Frame(self.master, width=150, height=50, bg='red', relief='ridge', bd=5)
        self.Inner_frame2.pack(pady=100)

        self.lbl1 = Label(self.Inner_frame1, text='Patient ID', font='Helvetica 15 bold',fg='blue',bg='black')
        self.lbl1.grid(row=0, column=0, pady=10, padx=10)
        self.lbl1_entry = Entry(self.Inner_frame1, width=30, font='Helvetica 15 bold', textvariable=self.pat_id)
        self.lbl1_entry.grid(row=0, column=1, pady=10, padx=10)
        self.lbl2 = Label(self.Inner_frame1, text='ROOM CHARGES', font='Helvetica 15 bold',fg='blue',bg='black')
        self.lbl2.grid(row=0, column=2, pady=10, padx=10)
        self.lbl2_entry = Entry(self.Inner_frame1, width=30, font='Helvetica 15 bold', textvariable=self.room_ch)
        self.lbl2_entry.grid(row=0, column=3, pady=10, padx=10)
        self.lbl3 = Label(self.Inner_frame1, text='DATE DISCHARGED(YYYY-MM-DD)', font='Helvetica 15 bold',fg='blue',bg='black')
        self.lbl3.grid(row=1, column=0, pady=10, padx=10)
        self.lbl3_entry = Entry(self.Inner_frame1, width=30, font='Helvetica 15 bold', textvariable=self.dat_dchr)
        self.lbl3_entry.grid(row=1, column=1, pady=10, padx=10)
        self.but4 = Button(self.Inner_frame1, text='UPDATE DISCHARGE DATE', font='Helvetica 15 bold',fg='blue', width=30, command=self.update_date)
        self.but4.grid(row=1, column=2,columnspan=2)
        self.lbl4 = Label(self.Inner_frame1, text='TREATMENT', font='Helvetica 15 bold',fg='blue',bg='black')
        self.lbl4.grid(row=2, column=0, pady=10, padx=10)
        self.lbl4_entry = Entry(self.Inner_frame1, width=30, font='Helvetica 15 bold', textvariable=self.treat)
        self.lbl4_entry.grid(row=2, column=1, pady=10, padx=10)
        self.lbl5 = Label(self.Inner_frame1, text='TREATMENT CODE', font='Helvetica 15 bold',fg='blue',bg='black')
        self.lbl5.grid(row=2, column=2, pady=10, padx=10)
        self.lbl5_entry = Entry(self.Inner_frame1, width=30, font='Helvetica 15 bold', textvariable=self.treat_cd)
        self.lbl5_entry.grid(row=2, column=3, pady=10, padx=10)
        self.lbl6 = Label(self.Inner_frame1, text='TREATMENT COST', font='Helvetica 15 bold',fg='blue',bg='black')
        self.lbl6.grid(row=3, column=0, pady=10, padx=10)
        self.lbl6_entry = Entry(self.Inner_frame1, width=30, font='Helvetica 15 bold', textvariable=self.treat_cs)
        self.lbl6_entry.grid(row=3, column=1, pady=10, padx=10)
        self.lbl7 = Label(self.Inner_frame1, text='MEDICINE', font='Helvetica 15 bold',fg='blue',bg='black')
        self.lbl7.grid(row=3, column=2, pady=10, padx=10)
        self.lbl7_entry = Entry(self.Inner_frame1, width=30, font='Helvetica 15 bold', textvariable=self.med)
        self.lbl7_entry.grid(row=3, column=3, pady=10, padx=10)
        self.lbl8 = Label(self.Inner_frame1, text='MEDICINE QUANTITY', font='Helvetica 15 bold',fg='blue',bg='black')
        self.lbl8.grid(row=4, column=0, pady=10, padx=10)
        self.lbl8_entry = Entry(self.Inner_frame1, width=30, font='Helvetica 15 bold', textvariable=self.med_qty)
        self.lbl8_entry.grid(row=4, column=1, pady=10, padx=10)
        self.lbl9 = Label(self.Inner_frame1, text='MEDICINE PRICE', font='Helvetica 15 bold',fg='blue',bg='black')
        self.lbl9.grid(row=4, column=2, pady=10, padx=10)
        self.lbl9_entry = Entry(self.Inner_frame1, width=30, font='Helvetica 15 bold', textvariable=self.med_prc)
        self.lbl9_entry.grid(row=4, column=3, pady=10, padx=10)

        self.but1 = Button(self.Inner_frame2, text='UPDATE DATA', font='Helvetica 15 bold',fg='blue', width=15, command=self.update_data)
        self.but1.grid(row=0, column=0)
        self.but2 = Button(self.Inner_frame2, text='GENERATE BILL', font='Helvetica 15 bold',fg='blue', width=15, command=self.generate_bill)
        self.but2.grid(row=0, column=1)
        self.but3 = Button(self.Inner_frame2, text='EXIT', font='Helvetica 15 bold', width=15,fg='blue', command=self.exit)
        self.but3.grid(row=0, column=2)

    def update_data(self):
        global b1,b2,b3,b4,b5,b6,b7,b8
        conn = sqlite3.connect("HMSDB.db")
        cursor = conn.cursor()
        b1 = (self.pat_id.get())
        b2 = (self.room_ch.get())
        b3 = (self.dat_dchr.get())
        b4 = (self.treat.get())
        b5 = (self.treat_cd.get())
        b6 = (self.treat_cs.get())
        b7 = (self.med.get())
        b8 = (self.med_prc.get())
        b9 = (self.med_qty.get())
        a = list(cursor.execute('select * from BILLING_INFO where Patient_ID = ?',(b1,)))
        x = len(a)
        if x!=0:
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM","PATIENT_ID IS ALREADY REGISTERED")   
        else:
            cursor.execute('insert into BILLING_INFO values(?,?,?,?,?,?,?,?,?)',(b1,b3,b4,b5,b6,b7,b8,b9,b2))
            conn.commit()
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM","BILLING DATA SAVED")
            

    def generate_bill(self):
        global b1
        conn = sqlite3.connect("HMSDB.db")
        cursor = conn.cursor()
        b1 = (self.pat_id.get())
        u = cursor.execute('select sum(TREATMENT_COST+ (M_COST*M_QTY) +ROOM_CHARGES) from BILLING_INFO where PATIENT_ID=?',(b1,))
        for i in u:
            self.xtralbl1 = Label(self.Inner_frame1, text='TOTAL AMOUNT OUTSTANDING', font='Helvetica 15 bold',bg='red')
            self.xtralbl1.grid(row=5, column=0, pady=10, padx=10)
            self.xtralbl2 = Label(self.Inner_frame1, text=i[0], font='Helvetica 15 bold',bg='red')
            self.xtralbl2.grid(row=5, column=1, pady=10)

    def update_date(self):
        global c1,c2
        conn = sqlite3.connect("HMSDB.db")
        conn.cursor()
        c1 = (self.pat_id.get())
        c2 =(self.dat_dchr.get())  
        conn.execute("UPDATE BILLING_INFO SET DISCHARGED=? where PATIENT_ID=?", (c2, c1,))
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
        conn.commit()

    def exit(self):
        self.master.destroy()





