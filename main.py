from tkinter import *
import winsound
import threading


# ---------------------------- SOUND ------------------------------- #
def play_sound():
    winsound.PlaySound('bgm1_passmngr.wav', winsound.SND_ASYNC | winsound.SND_LOOP)

def toggle_sound():
        if sound_var.get():
            sound_thread = threading.Thread(target=play_sound)
            sound_thread.start()
        else:
            winsound.PlaySound(None, winsound.SND_ASYNC)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get() 
    
    with open("password_data.txt","a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(140,100, image=logo_img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0) 
sound_label = Label(text="Sound?")

#Boolean
sound_var = BooleanVar()

#Entries
website_entry = Entry(width=52)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(0, "fillyouremail@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3,column=2, columnspan=1)
add_button = Button(text="Add", width=44, command = save)
add_button.grid(row=4, column=1, columnspan=2)
sound_checkbox = Checkbutton(text="BGM", variable = sound_var, command=toggle_sound)
sound_checkbox.grid(row=0,column=3)

window.mainloop()

