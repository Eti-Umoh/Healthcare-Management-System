from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
from PIL import ImageTk, Image

conn = sqlite3.connect("HMSDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

class Appointment:
    def __init__(self, master):
        self.master = master
        self.master.title("HEALTHCARE MANAGEMENT SYSTEM")
        self.master.geometry("2600x1500")
        # self.frame = Frame(self.master)
        # self.frame.pack()

        image1 = Image.open("static/healthcare-medical-cartoon-vector-245128553.jpg")
        test = ImageTk.PhotoImage(image1)
        img_lbl = Label(self.master,image = test)
        img_lbl.image = test
        img_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        self.pat_ID = IntVar()
        self.emp_ID = IntVar()
        self.ap_no = IntVar()
        self.ap_time = StringVar()
        self.ap_date = StringVar()
        self.des = StringVar()

        self.lblTitle = Label(self.master, text="APPOINTMENT FORM", font="Helvetica 20 bold",fg='red',bg='sky blue')
        self.lblTitle.pack(pady=50)

        self.LoginFrame = Frame(self.master, width=400, height=80, relief="ridge", bg="sky blue", bd=5)
        self.LoginFrame.pack()

        self.LoginFrame2 = Frame(self.master, width=400, height=80, relief="ridge", bg="red", bd=5)
        self.LoginFrame2.pack(pady=100)

        # ===========LABELS=============
        self.lblpid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold",fg='red',bg='sky blue', bd=22)
        self.lblpid.grid(row=0, column=0)
        self.lblpid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_ID)
        self.lblpid.grid(row=0, column=1)

        self.lbldid = Label(self.LoginFrame, text="DOCTOR ID", font="Helvetica 14 bold",fg='red',bg='sky blue' , bd=22)
        self.lbldid.grid(row=1, column=0)
        self.lbldid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_ID)
        self.lbldid.grid(row=1, column=1)

        self.lblap = Label(self.LoginFrame, text="APPOINTMENT NO", font="Helvetica 14 bold",fg='red',bg='sky blue', bd=22)
        self.lblap.grid(row=2, column=0)
        self.lblap = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_no)
        self.lblap.grid(row=2, column=1)

        self.lblapt = Label(self.LoginFrame, text="APPOINTMENT TIME(HH:MM:SS)", font="Helvetica 14 bold",fg='red',bg='sky blue', bd=22)
        self.lblapt.grid(row=0, column=2)
        self.lblapt = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_time)
        self.lblapt.grid(row=0, column=3)

        self.lblapd = Label(self.LoginFrame, text="APPOINTMENT DATE(YYYY-MM-DD)", font="Helvetica 14 bold",fg='red',bg='sky blue' , bd=22)
        self.lblapd.grid(row=1, column=2)
        self.lblapd = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_date)
        self.lblapd.grid(row=1, column=3)

        self.lbldes = Label(self.LoginFrame, text="DESCRIPTION", font="Helvetica 14 bold",fg='red',bg='sky blue', bd=22)
        self.lbldes.grid(row=2, column=2)
        self.lbldes = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.des)
        self.lbldes.grid(row=2, column=3)

        self.button2 = Button(self.LoginFrame2, text="SAVE", width=10, font="Helvetica 14 bold",fg='red', command=self.INSERT_AP)
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold",fg='red', command=self.DE_AP_DISPLAY)
        self.button3.grid(row=3, column=2)

        self.button3 = Button(self.LoginFrame2, text="SEARCH APPOINTMENTS", width=20, font="Helvetica 14 bold",fg='red', command=self.S_AP_DISPLAY)
        self.button3.grid(row=3, column=3)

        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold",fg='red', command=self.Exit)
        self.button6.grid(row=3, column=4)

    def Exit(self):
        self.master.destroy()

    def INSERT_AP(self):
        global e1, e2, e3, e4, e5, e6, var
        e1 = (self.pat_ID.get())
        e2 = (self.emp_ID.get())
        e3 = (self.ap_no.get())
        e4 = (self.ap_time.get())
        e5 = (self.ap_date.get())
        e6 = (self.des.get())
        conn = sqlite3.connect("HMSDB.db")
        p = list(conn.execute("SELECT * FROM APPOINTMENT_INFO WHERE APPOINTMENT_NO =?", (e3,)))
        x = len(p)
        if x != 0:
            tkinter.messagebox.showerror("HEALTHCARE DATABSE SYSTEM", "APPOINTMENT ALREADY EXISTS")
        else:
            conn.execute("Insert into APPOINTMENT_INFO values(?,?,?,?,?,?)", (e1, e3, e2, e5, e6, e4,))
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM", "APPOINTMENT SET SUCCSESSFULLY")
        conn.commit()

    def DE_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DEL_APP(self.newWindow)

    def S_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = SEA_APP(self.newWindow)


# CLASS FOR DISPLAY MENU FOR DELETE APPOINTMENT
class DEL_APP:
    def __init__(self, master):
        global de1_app, de
        self.master = master
        self.master.title("HEALTHCARE MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.del_ap = StringVar()
        self.lblTitle = Label(self.frame, text="DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="red", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="red", bd=20)
        self.LoginFrame2.grid(row=2, column=0,pady=10)

        self.lblpatid = Label(self.LoginFrame, text="ENTER APPOINTMENT NO TO DELETE", font="Helvetica 14 bold",
                              bg="red", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.del_ap)
        self.lblpatid.grid(row=0, column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", command=self.DELETE_AP)
        self.DeleteB.grid(row=3, column=1)

    def DELETE_AP(self):
        global inp_d
        inp_d = str(self.del_ap.get())
        conn = sqlite3.connect("HMSDB.db")
        v = list(conn.execute("select * from APPOINTMENT_INFO where APPOINTMENT_NO=?", (inp_d,)))
        if (len(v) == 0):
            tkinter.messagebox.showerror("HEALTHCARE DATABSE SYSTEM", "PATIENT APPOINTMENT NOT FIXED")
        else:
            conn.execute('DELETE FROM APPOINTMENT_INFO where APPOINTMENT_NO=?', (inp_d,))
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")
        conn.commit()


class SEA_APP:
    def __init__(self, master):
        global inp_s, ap_date, SearchB
        self.master = master
        self.master.title("HEALTHCARE MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.ap_date = StringVar()
        self.lblTitle = Label(self.frame, text="SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=25)

        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="red", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="red", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # ===========LABELS=============
        self.lblpatid = Label(self.LoginFrame, text="ENTER DATE TO VIEW APPOINTMENTS(YYYY-MM-DD)",
                              font="Helvetica 14 bold", bg="red", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_date)
        self.lblpatid.grid(row=0, column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", command=self.SEARCH_AP)
        self.SearchB.grid(row=0, column=1)

    def SEARCH_AP(self):
        global inp_s, ap_date, errorS, t, i, q, dis1, dis2, dis3, dis4, dis5, dis6, dis7, dis8, dis9, dis10, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10
        c1 = conn.cursor()
        ap = (self.ap_date.get())
        p = list(c1.execute("select * from APPOINTMENT_INFO where DOA=?", (ap,)))
        if (len(p) == 0):
            tkinter.messagebox.showerror("HEALTHCARE DATABSE SYSTEM", "THERE'S NO APPOINTMENT BOOKED")
        else:
            t = c1.execute(
                'SELECT PATIENT_ID,PATIENT_NAME,APPOINTMENT_NO,DOCTOR_ID,DOA,APPOINT_TIME,DESCRIPTION FROM PATIENT_INFO NATURAL JOIN APPOINTMENT_INFO where DOA=?',
                (ap,))
            for i in t:
                self.l1 = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="red", bd=22)
                self.l1.grid(row=1, column=0)
                self.dis1 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="red", text=i[0])
                self.dis1.grid(row=1, column=1)
                self.l2 = Label(self.LoginFrame, text="PATIENT NAME", font="Helvetica 14 bold", bg="red", bd=22)
                self.l2.grid(row=2, column=0)
                self.dis2 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="red", text=i[1])
                self.dis2.grid(row=2, column=1)

                self.l3 = Label(self.LoginFrame, text="APPOINTMENT NO", font="Helvetica 14 bold", bg="red",
                                bd=22)
                self.l3.grid(row=3, column=0)
                self.dis3 = Label(self.LoginFrame, font="Helvetica 14 bold", bg="red", bd=2, text=i[2])
                self.dis3.grid(row=3, column=1)

                self.l4 = Label(self.LoginFrame, text="DOCTOR ID", font="Helvetica 14 bold", bg="red", bd=22)
                self.l4.grid(row=4, column=0)
                self.dis4 = Label(self.LoginFrame, font="Helvetica 14 bold", bg="red", bd=2, text=i[3])
                self.dis4.grid(row=4, column=1)

                self.l5 = Label(self.LoginFrame, text="APPOINTMENT TIME(HH:MM:SS)", font="Helvetica 14 bold",
                                bg="red", bd=22)
                self.l5.grid(row=5, column=0)
                self.dis5 = Label(self.LoginFrame, font="Helvetica 14 bold", bg="red", bd=2, text=i[5])
                self.dis5.grid(row=5, column=1)




