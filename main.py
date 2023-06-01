import tkinter as tk
import users
from windows.user_window import *
from windows.admin_window import *
from PIL import ImageTk, Image
import random

WIDTH = 800
HEIGHT = 600
packnames = ["Base Set", "Rebel Clash", "Darkness Ablaze", "Champion's Path", "Vivid Voltage", 
            "Shining Fates", "Battle Styles", "Chilling Reign", "Evolving Skies", "Fusion Strike",
            "Astral Radiance", "Brilliant Stars", "Lost Origin", "Silver Tempest"]

def close():
    exit()

def close_prog(e):
    exit()

#have folder full of starters
#know names of starters, get random member of list
starter_list = ["bulbasaur", "squirtle", "charmander", "chikorita", "chimchar", "cyndaquil", "mudkip", "oshawott", "piplup", "snivy",
                "tepig", "torchic", "totodile", "treecko", "turtwig"]

rand_num = random.randint(0, len(starter_list)-1)
poke = starter_list[rand_num]

emma = users.get_emma() 
alex = users.get_alex()

font_pkm = ("Pixeloid Sans", 40)

start = tk.Tk(className="Pokémon Card Tracker")
start.configure(background="#74e7fc")
start.attributes('-fullscreen',True)

ws = start.winfo_screenwidth() # width of the screen
hs = start.winfo_screenheight() # height of the screen
x = (ws/2) - (WIDTH/2)
y = (hs/2) - (HEIGHT/2)

start.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

canvas = tk.Canvas(start, width=2000, height=2000, highlightthickness=0)
canvas.pack()

background_img = ImageTk.PhotoImage(Image.open("./assets/background.png").resize((1570, 920)))
bg = canvas.create_image(0, 0, image=background_img, anchor=tk.NW)

canvas.create_text(720, 150, text="Welcome to the Pokémon Organizer!", font=font_pkm)
canvas.create_text(720, 220, text="Please select a user.", font=("Pixeloid Sans", 30))

photo_may = ImageTk.PhotoImage(Image.open("./assets/may64.png"))
photo_brendan = ImageTk.PhotoImage(Image.open("./assets/brendan64.png")) 
photo_turtwig = ImageTk.PhotoImage(Image.open("./assets/starters/" + poke + ".png").resize((160, 160)))
may_button = canvas.create_image(440, 500, image=photo_may)
bren_button = canvas.create_image(1000, 500, image=photo_brendan)
turtwig_button = canvas.create_image(720, 550, image=photo_turtwig)
canvas.tag_bind(may_button, '<Button-1>', lambda e: window_setup(start, "Emma", emma))
canvas.tag_bind(bren_button, '<Button-1>', lambda e: window_setup(start, "Alex", alex))
canvas.tag_bind(turtwig_button, '<Button-1>', lambda e: admin_setup(start))
canvas.create_text(450, 650, text="Emma", font=("Pixeloid Sans", 30))
canvas.create_text(1000, 650, text="Alex", font=("Pixeloid Sans", 30))
canvas.create_text(730, 650, text="Admin", font=("Pixeloid Sans", 30))

quit = tkm.Button(start, bg="#a7f3fc", borderless=True, height=40, width=90, font=("Pixeloid Sans", 12), 
                  text = "Quit", activebackground="#a7f3fc", focuscolor="#a7f3fc", command=close)
quit.place(relx=0, rely=0.0, anchor="nw")

#may_button = tkm.Button(start, focuscolor='', command=lambda : window_setup(start, "Emma", emma, packs), image = photo_may).pack(side = tk.LEFT, padx = 250, expand=tk.NO)
#bren_button = tkm.Button(start, focuscolor='', command=lambda : window_setup(start, "Alex", alex, packs), image = photo_brendan).pack(side = tk.RIGHT, padx = 250, expand=tk.NO)

photo_buizel = tk.PhotoImage(file = "./assets/buizel.png")
start.iconphoto(True, photo_buizel)

# Bind the function to configure the parent window
start.bind('<Escape>',close_prog)
start.mainloop()
