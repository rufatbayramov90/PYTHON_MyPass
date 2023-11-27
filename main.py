from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=60,pady=60)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website : ")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/UserName : ")
email_label.grid(row=2,column=0)
password_label = Label(text="Password : ")
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=45)
website_entry.grid(row=1,column=1, columnspan = 2)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(row=2,column=1, columnspan = 2)
email_entry.insert(0, "rufatbyrmv@gmail.com")
password_entry = Entry(width=27)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add", width = 38, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()