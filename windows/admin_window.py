import tkinter as tk
import shutil
from tkinter import filedialog
from PIL import ImageTk, Image
import tkmacosx as tkm
import users as users

blue = "#38a7b8"
lightblue ="#60c0bf"
darkblue ="#1b7987"

def close_prog(event):
    exit()

def close_window(curr, main):
    main.deiconify()
    curr.destroy()

def upload_txt(curr):
    filename = filedialog.askopenfilename()
    if filename.endswith(".txt"):
        shutil.move(filename, "./files/cardpacks")
        warning = tk.Label(curr, bg=blue, text="WARNING:\nBe careful with this command! Adding the wrong\nfile or pack name is currently not fixable!", fg="#ffffff", font = ("Pixeloid Sans", 20))
        warning.place(relx=0.75, rely=0.42, anchor=tk.CENTER)
        search_bar = tk.Entry(curr, font=("Pixeloid Sans", 20), bd=0, borderwidth=0.01)
        search_bar.place(relx=0.75, rely=0.5, anchor="center")

        def add_text():
            file = open("./files/packnames.txt", "a", encoding='utf-8-sig')
            new_name = search_bar.get()
            if len(new_name) != 0:
                file.write("\n"+new_name)
                file.close() 
                confirm = tk.Label(curr, bg=blue, text="New List Added!", fg="#ffffff", font = ("Pixeloid Sans", 20))
                confirm.place(relx=0.75, rely=0.52, anchor=tk.CENTER)
            warning.destroy()
            search_bar.destroy()
            enter_button.destroy()
        
        enter_button = tkm.Button(curr, font=("Pixeloid Sans", 15), bg=lightblue, height=35, width=70,
                                  text="Submit", fg="#ffffff", borderless=True, activebackground=darkblue, 
                                  focuscolor="", command= add_text)
        enter_button.place(relx=0.75, rely=0.55, anchor="center")

def admin_setup(start):
    #add pack to all users

    admin = tk.Toplevel(bg=blue)
    admin.title("Pokémon Card Tracker")
    admin.attributes('-fullscreen',True)

    background_img = ImageTk.PhotoImage(Image.open("./assets/snow_background.png").resize((1570, 920)))
    bkgd = tk.Label(admin, image=background_img)
    bkgd.image = background_img
    bkgd.configure(image=background_img)
    bkgd.place(x=-5, y=-5)

    pack = tkm.Button(admin, borderless=True, font=("Pixeloid Sans", 15), bg=lightblue, height=60, width=200,
                     text="Add new global pack", fg="#ffffff", activebackground=darkblue, focuscolor="",
                    command=lambda: upload_txt(admin))
    pack.place(relx=0.65, rely=0.3, anchor="center")
    
    back = tkm.Button(admin, bg=lightblue, height=40, width=90, borderless=True, font=("Pixeloid Sans", 12), 
                      text = "Back to\nUser Select", activebackground=darkblue, focuscolor="", 
                      command=lambda : close_window(admin, start))
    back.place(relx=0.42, rely=0.03, anchor="center")

    welcome = tk.Label(admin, bg=blue, text="Admin Controls", fg="#ffffff")
    welcome.configure(font = ("Pixeloid Sans", 30))
    welcome.place(relx=0.75, rely=0.2, anchor=tk.CENTER)

    credit = tk.Label(admin, bg=blue, text="Created by Emma Scalabrino", fg="#ffffff")
    credit.configure(font = ("Pixeloid Sans", 15))
    credit.place(relx=0.75, rely=0.9, anchor="center")

    admin.bind('<Escape>',close_prog)
