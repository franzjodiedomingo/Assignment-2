from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Register')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='reg.png')
Label(root, image=img, bg='white').place(x=50, y=50) 

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

def complete():
    global Age, address  
    user_age = Age.get()
    user_address = address.get()

    if user_age != '' and user_address != '':
        frame = Frame(root, width=500, height=500, bg="white")
        frame.place(x=500, y=70)

        frame = Frame(root, width=500, height=500, bg="white")
        frame.place(x=-50, y=70)

        Label(text='You are now registered!', bg='white', font=('Calibri (Body)', 50, 'bold')).pack(expand=True)


def next():
    last_name = lastname.get()
    first_name = firstname.get()
    middle_name = middlename.get()

    if last_name != '' and first_name != '' and middle_name != '':
        Label(root, image=img, bg='white').place(x=50, y=50)  

        frame = Frame(root, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        heading = Label(frame, text='Personal Details', fg='#ea4051', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=55, y=3)

        def on_enter_age(e):
            Age.delete(0, 'end')

        def on_leave_age(e):
            name = Age.get()
            if name == '':
                Age.insert(0, 'Age')

        global Age  # Declare Age as a global variable
        Age = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        Age.place(x=30, y=75)
        Age.insert(0, 'Age') 
        Age.bind('<FocusIn>', on_enter_age)
        Age.bind('<FocusOut>', on_leave_age)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=100)

        def on_enter_address(e):
            address.delete(0, 'end')

        def on_leave_address(e):
            name = address.get()
            if name == '':
                address.insert(0, 'Address')

        global address  # Declare address as a global variable
        address = Entry(frame, width=50, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        address.place(x=30, y=140)
        address.insert(0, 'Address')
        address.bind('<FocusIn>', on_enter_address)
        address.bind('<FocusOut>', on_leave_address)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=165)

        Button(frame, width=39, pady=7, text='Complete', bg='#ea4051', fg='white', border=0, command=complete).place(x=35, y=260)

heading = Label(frame, text='Sign up', fg='#ea4051', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=115, y=3)

def on_enter_lastname(e):
    lastname.delete(0, 'end')

def on_leave_lastname(e):
    name = lastname.get()
    if name == '':
        lastname.insert(0, 'Last name')

lastname = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
lastname.place(x=30, y=75)
lastname.insert(0, 'Last name') 
lastname.bind('<FocusIn>', on_enter_lastname)
lastname.bind('<FocusOut>', on_leave_lastname)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=100)

def on_enter_firstname(e):
    firstname.delete(0, 'end')

def on_leave_firstname(e):
    name = firstname.get()
    if name == '':
        firstname.insert(0, 'First name')

firstname = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
firstname.place(x=30, y=140)
firstname.insert(0, 'First name')
firstname.bind('<FocusIn>', on_enter_firstname)
firstname.bind('<FocusOut>', on_leave_firstname)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=165)

def on_enter_middlename(e):
    middlename.delete(0, 'end')

def on_leave_middlename(e):
    name = middlename.get()
    if name == '':
        middlename.insert(0, 'Middle name')

middlename = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
middlename.place(x=30, y=205)
middlename.insert(0, 'Middle name')
middlename.bind('<FocusIn>', on_enter_middlename)
middlename.bind('<FocusOut>', on_leave_middlename)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=230)

Button(frame, width=39, pady=7, text='Next', bg='#ea4051', fg='white', border=0, command=next).place(x=35, y=260)
label = Label(frame, text="Already have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=70, y=300)

sign_in = Button(frame, width=6, text="Sign in", border=0, bg='white', cursor='hand2', fg='#ea4051')
sign_in.place(x=215, y=300)

root.mainloop()