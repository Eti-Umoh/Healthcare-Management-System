import sqlite3

conn = sqlite3.connect("HMSDB.db")
cursor = conn.cursor()

# cursor.execute('Drop table if exists LOGIN')
# stmt = 'create table LOGIN (Usernames varchar(20),Password int(4),Role varchar(15))'
# cursor.execute(stmt)


# cursor.execute('Drop table if exists PATIENT_INFO')
# stmt = 'create table PATIENT_INFO (Patient_ID int(5) primary key, Patient_name varchar(20),Address varchar(50),Sex varchar(7),Email varchar(20),Blood_Group varchar(5),DOB date,Contact_NO varchar(12))'
# cursor.execute(stmt)

# cursor.execute('Drop table if exists APPOINTMENT_INFO')
# stmt = 'create table APPOINTMENT_INFO (Patient_ID int(5),Appointment_NO int(5) primary key,Doctor_ID int(5),DOA date,Description varchar(50),Appoint_time time, Foreign key(Patient_ID) references PATIENT_INFO(Patient_ID))'
# cursor.execute(stmt)

# cursor.execute('Drop table if exists ROOM')
# stmt = 'create table ROOM (Patient_ID int(5),Room_NO int(5) primary key,Room_type int(5),Room_charges int(5),Admitted date,Discharged date,Foreign key(Patient_ID) references PATIENT_INFO(Patient_ID))'
# cursor.execute(stmt)

# cursor.execute('Drop table if exists PATIENT_RECORD')
# stmt = 'create table PATIENT_RECORD(Patient_ID int(5) primary key,Patient_name varcahar(20),Medication varcahar(50),Illness varchar(50),Operation varchar(20),Operation_date date,Operation_time time,Foreign key(Patient_ID) references PATIENT_INFO(Patient_ID))'
# cursor.execute(stmt)

# cursor.execute('Drop table if exists BILLING_INFO')
# stmt = 'create table BILLING_INFO(Patient_ID int(5) primary key,Discharged date,Treatment varchar(20),Treatment_code int(5),Treatment_cost decimal(15,2),Medicine varchar(12),M_cost decimal(7,2),M_qty int(2),Room_charges int(5),Foreign key(Patient_ID) references PATIENT_INFO(Patient_ID),Foreign key(Room_charges) references ROOM(Room_charges))'
# cursor.execute(stmt)


conn.commit()

cursor.close()
conn.close()