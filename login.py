from tkinter import *
import os
from cryptography.fernet import Fernet
from PIL import ImageTk
import random
import smtplib
 
creds = 'teMpf1le.temp' 
login_email="gmail" #enter your valid gmail id 
login_paswd="paswword" #enter your password of gmail is which you have given above

 
def Signup(): 
    global pwordE 
    global nameE
    global roots
    global emailE
    global s
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls() 
    s.login(login_email, login_paswd)
    roots = Tk()
    roots.geometry('700x500') 
    roots.title('Signup') 
    roots.bg=ImageTk.PhotoImage(file="bac_3.jpg")
    bg_lbl=Label(roots,image=roots.bg).place(x=0, y=0, relwidth=1, relheight=1)
    intruction = Label(roots, text='Please Enter new Credidentials\n',font=("algerian",15),bg='#1E4F6B') 
    intruction.grid(row=0, column=1)
    nameL = Label(roots, text='New Username: ',font=("times new roman",12),bg='#558098') 
    pwordL = Label(roots, text='New Password: ',font=("times new roman",12),bg='#558098') 
    email = Label(roots, text='Email id: ',font=("times new roman",12),bg='#558098') 
    lbl2=Label(roots,text='').grid(row=1,column=1)
    lbl3=Label(roots,text='').grid(row=2,column=1)
    nameL.grid(row=3, column=0,)
    pwordL.grid(row=4, column=0,) 
    email.grid(row=5, column=0,) 

    nameE = Entry(roots)
    pwordE = Entry(roots, show='*') 
    emailE = Entry(roots)
    nameE.grid(row=3, column=1) 
    pwordE.grid(row=4, column=1) 
    emailE.grid(row=5,column=1)
    lbl1=Label(roots,text='').grid(row=6,column=1)
    signupButton = Button(roots, text='Signup', command=FSSignup) 
    signupButton.grid(row=7, column=1,columnspan=2, sticky=W)
    roots.mainloop() 
 
def FSSignup():
    
    with open(creds, 'wb') as f: 
        key=Fernet.generate_key()
        y=Fernet(key)
        num=random.randint(1111,9999)
        email_1=emailE.get()
        mess=str(num)
        message = mess
        s.sendmail(login_email, email_1, message)
        name_1=nameE.get()
        pword_1=pwordE.get()
        line="\n"
        newline=line.encode()
        name_2=name_1.encode()
        pword_2=pword_1.encode()
        mess_1=mess.encode()
        messM=y.encrypt(mess_1)
        nameN=y.encrypt(name_2)
        pwordP=y.encrypt(pword_2)
        f.write(nameN) 
        f.write(newline) 
        f.write(pwordP) 
        f.write(newline)
        f.write(messM)
        f.write(newline)
        f.write(key)
        f.close() 
        s.quit() 
 
    roots.destroy() 
    Login()
 
def Login():
    global nameEL
    global pwordEL 
    global rootA
    global codeL
    
    rootA = Tk() 
    rootA.geometry('700x500') 
    rootA.title('Login') 
    rootA.bg=ImageTk.PhotoImage(file="bac_2.jpg")
    bg_lbl1=Label(rootA,image=rootA.bg).place(x=0, y=0, relwidth=1, relheight=1)
 
    intruction = Label(rootA, text='Login\n') 
    intruction.grid(sticky=E) 
 
    nameL = Label(rootA, text='Username: ') 
    pwordL = Label(rootA, text='Password: ') 
    codeL = Label(rootA, text='code: ')
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
    codeL.grid(row=3, sticky=W)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    codeL = Entry(rootA) 
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
    codeL.grid(row=3,column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) 
    loginB.grid(columnspan=2, sticky=W)
 
    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) 
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()
 
def CheckLogin():
    with open(creds, 'rb') as f:
        data = f.readlines() 
        enc_name = data[0].rstrip() 
        enc_pword = data[1].rstrip()
        code_1 = data[2].rstrip()
        keym=data[3].rstrip()
        print(keym)
        x=Fernet(keym)
        dec_name = x.decrypt(enc_name)
        dec_pword = x.decrypt(enc_pword)
        dec_code = x.decrypt(code_1)
        uname=dec_name.decode()
        pword=dec_pword.decode()
        code = dec_code.decode()
 
    if nameEL.get() == uname and pwordEL.get() == pword and codeL.get()==code  :
            r = Tk() 
            r.title(':D')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[+] Logged In') 
            rlbl.pack() 
            r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
 
def DelUser():
    os.remove(creds) 
    rootA.destroy() 
    Signup() 
 
if os.path.isfile(creds):
    Login()
else: 
    Signup()
