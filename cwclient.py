import tkinter as tk
from tkinter import *
from tkinter import messagebox
import socket


HOST = '127.0.0.1'
PORT = 65430
# Create a server socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect
client_socket.connect((HOST, PORT))

#create a new window to ask the username and password
first = Tk()
first.geometry("500x500")
first.title("Welcome")
first.configure(bg='white')
username = Label(first, text="Username:", font=("Georgia", 12, "bold"),
                  fg='dark slate gray', bg='white').place(x=10, y=100)
user = Entry(first, width=40)
user.place(x=110, y=100)
passw=Label(first, text="Password:", font=("Georgia", 12, "bold"),
                  fg='dark slate gray', bg='white').place(x=10, y=200)
password=Entry(first, width=40, show='*')
password.place(x=110, y=200)



def sh():
    while password.configure(show='*'):
        see = Button(first, text='hide', command=password.configure(show=NONE)).place(x=400, y=200)
    else:
        see= Button(first, text='hide', command=password.configure(show="*")).place(x=400, y=200)

see=Button(first, text='show', command=sh)
see.place(x=400, y=200)


def addclient():
    global name
    global position
    client=Tk()
    client.geometry("500x500")
    client.title("Add a Client")
    namelabel= Label(client, text="Enter client's name:", font=("Georgia", 12, "bold"),
                  fg='dark slate gray', bg='white').place(x=10, y=100)
    geographicalposition=Label(client, text="Enter position in the shop:", font=("Georgia", 12, "bold"),
                  fg='dark slate gray', bg='white').place(x=10, y=300)
    name=Entry(client, width=40)
    position=Entry(client, width=40)
    name.place(x=110, y=200)
    position.place(x=110, y=400)
    client_socket.send('client'.encode("utf-8"))
    def sendclient():
        client.withdraw
        try:
            name1=name.get()
            position1=position.get()
            msg3=client_socket.recv(1024).decode("utf-8")
            if msg3 == "clientinfo":
                client_socket.send(name1.encode("utf-8"))
                client_socket.send(position1.encode("utf-8"))
                msg1=client_socket.recv(1024).decode("utf-8")
                if msg1 == "received":
                    text = "Client added to the system!"
                    box = Tk()
                    message = Label(box, text=text, font=("Times New Roman", 15, 'bold')).place(x=10, y=10)
                    close = Button(box, text="Close", command=client.withdraw).place(x=50, y=100)
                    box.mainloop()
                else:
                    text="Please try again, there was an error"
                    box = Tk()
                    message = Label(box, text=text, font=("Times New Roman", 15, 'bold')).place(x=10, y=10)
                    close = Button(box, text="Close", command=box.withdraw).place(x=50, y=100)
                    box.mainloop()
        except:
            messagebox.showerror("errorWindow", "oops! Error, PLease try again!")


    cont = Button(client, text="Continue", command=sendclient)
    cont.place(x=110, y=450)
    client.mainloop()


def currentstock():
    pass

def order():
    pass


def cdashboard():
    cl=Tk()
    cl.geometry("500x500")
    cl.title("Client Dashboards")
    choose=Label(cl, text= "Choose a client:").place(x=200, y=200)
    mnu=Menubutton.place(x=200, y=300)


def sdashboard():
    pass

def dashboards():
    db=Tk()
    db.geometry("500x500")
    db.title("Dashboards")
    db.configure(bg='white')
    cd=Button(db, text="Client Dashboard", command=cdashboard).place(x=200, y=200)
    sd= Button(db, text="Your Dashboard", command=sdashboard).place(x=200, y=300)


def mainmenu():
    first.withdraw()
    main=Toplevel(first)
    main.geometry("500x500")
    main.title("Main Menu")
    main.configure(bg='white')
    name=Menubutton(main, text=f"{fullname}").place(x=380,y=0)
    Var1 = IntVar()
    Menu1 = Menu(name, tearoff=0)
    Menu1.add_radiobutton(label="View dashboard", variable=Var1, value=1)
    Menu1.add_radiobutton(label="Change account settings", variable=Var1, value=2)
    Menu1.add_radiobutton(label="Log out", variable=Var1, value=3)
    add=Button(main, text="Add a client", command=addclient).place(x=10, y=100)
    cstock = Button(main, text="Show current stock", command=currentstock).place(x=10, y=200)
    ord = Button(main, text="Place an Order", command=order).place(x=10, y=300)
    dash = Button(main, text="Dashboards", command=dashboards).place(x=10, y=400)
    choose=Label(main, text="Choose a section of the shop:").place(x=200, y=50)
    clothespic=PhotoImage(file="OIP.png")
    pic1=Button(main, text="clothing", fg='white', image=clothespic).place(x=200, y=100)
    status1 = Label(main, text="☻: ", fg='green', font=(15)).place(x=200, y=235)
    status11 = Label(main, text="☺: ", fg='red', font=(15)).place(x=255, y=235)
    techno=PhotoImage(file="OIP1.png")
    pic2=Button(main, text="techno", image=techno).place(x=200, y=260)
    status2 = Label(main, text="☻: ", fg='green', font=(15)).place(x=200, y=400)
    status21 = Label(main, text="☺: ", fg='red', font=(15)).place(x=255, y=400)
    furniture = PhotoImage(file="OIP2.png")
    pic3 = Button(main, text="furniture", image=furniture).place(x=330, y=100)
    status3 = Label(main, text="☻: ", fg='green', font=(15)).place(x=335, y=270)
    status31=Label(main, text="☺: ", fg='red', font=(15)).place(x=390, y=270)
    status = Label(main, text="Total number of clients in the shop: {}").place(x=200, y=450)
    statuss = Label(main, text="☻: ", fg='green', font=(15)).place(x=200, y=470)
    statuss1 = Label(main, text="☺: ", fg='red', font=(15)).place(x=255, y=470)
    main.mainloop()

def error():
    errors=Tk()
    message=Label(errors, text="Wrong username \n or password \n Please try Again", font=("Times New Roman", 15, 'bold')).place(x=10, y=10)
    close=Button(errors, text="Close", command=errors.withdraw).place(x=50, y=100)
    errors.mainloop()

def login():
    try:
        global fullname
        user1 = user.get()
        password1 = password.get()
        msg=client_socket.recv(1024).decode('utf-8')
        if msg == "user":
            client_socket.send(user1.encode('utf-8'))
            msg2=client_socket.recv(1024).decode('utf-8')
            if msg2=="password":
                client_socket.send(password1.encode('utf-8'))
                msg3 = client_socket.recv(1024).decode('utf-8')
                if msg3=="good":
                    sname=client_socket.recv(1024).decode('utf-8')
                    surname=client_socket.recv(1024).decode('utf-8')
                    fullname=f"{sname + surname}"
                    mainmenu()
                else:
                    error()
            else:
                error()
        else:
            error()
    except:
        messagebox.showerror("errorWindow", "oops! Error, PLease try again!")


cont=Button(first, text="Continue", command=login)
cont.place(x=110, y=300)



first.mainloop()
client_socket.close()