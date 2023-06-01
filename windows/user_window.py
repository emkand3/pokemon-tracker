import tkinter as tk
from PIL import ImageTk, Image
import tkmacosx as tkm
import users as users

pack_dict = {}
current_widgets = []
list_data = []
green = "#c1d9ad"
username = "none"
highlight = "#a8c490"
packnames = []
packlist = []

def handler(function, curr, userlist, packlist):
    for x in current_widgets:
        x.destroy()
    current_widgets.clear()
    function(curr, userlist, packlist)

def dict_setup(packlist, userlist):
    matches = 0
    matchVec = []
    for list in packlist:
        for i in userlist:
            for pkm in list:
                if i == pkm:
                    matches+=1
        matchVec.append(matches)
        matches = 0
    for x in range(len(matchVec)):
        pack_dict[packnames[x]] = matchVec[x]

def update(list, data):
    list.delete(0, tk.END)
    for items in data:
        list.insert(tk.END, items)

def close_prog(event):
    exit()

def close_window(curr, main):
    main.deiconify()
    curr.destroy()

def tiered_list(curr, userlist, packlist):
    matchNums = []
    packstrs = []
    for key in pack_dict:
        matchNums.append(pack_dict[key])
        packstrs.append(key)
    sortedNums = sorted(matchNums)

    index_last= matchNums.index(sortedNums[0])
    last = packstrs[index_last]
    packstrs.remove(packstrs[index_last])
    matchNums.remove(matchNums[index_last])

    index_last2= matchNums.index(sortedNums[1])
    last2 = packstrs[index_last2]
    packstrs.remove(packstrs[index_last2])
    matchNums.remove(matchNums[index_last2])

    index_last3= matchNums.index(sortedNums[2])
    last3 = packstrs[index_last3]
    packstrs.remove(packstrs[index_last3])
    matchNums.remove(matchNums[index_last3])

    index_third= matchNums.index(sortedNums[len(sortedNums)-3])
    third = packstrs[index_third]
    packstrs.remove(packstrs[index_third])
    matchNums.remove(matchNums[index_third])

    index_second= matchNums.index(sortedNums[len(sortedNums)-2])
    second = packstrs[index_second]
    packstrs.remove(packstrs[index_second])
    matchNums.remove(matchNums[index_second])

    index_first= matchNums.index(sortedNums[len(sortedNums)-1])
    first = packstrs[index_first]
    packstrs.remove(packstrs[index_first])
    matchNums.remove(matchNums[index_first])

    firstS = first + ": " + str(sortedNums[len(sortedNums)-1]) + " matches."
    secondS = second + ": " + str(sortedNums[len(sortedNums)-2]) + " matches."
    thirdS = third + ": " + str(sortedNums[len(sortedNums)-3]) + " matches."
    worst1 = last + ": " + str(sortedNums[0]) + " matches."
    worst2 = last2 + ": " + str(sortedNums[1]) + " matches."
    worst3 = last3 + ": " + str(sortedNums[2]) + " matches."

    top3 = tk.Label(curr, font=("Pixeloid Sans", 20), text="Best 3 Packs:", bg=green)
    top3.place(relx=0.37, rely=0.45, anchor="center")
    current_widgets.append(top3)
    bad3 = tk.Label(curr, font=("Pixeloid Sans", 20), text="Worst 3 Packs:", bg=green)
    bad3.place(relx=0.61, rely=0.45, anchor="center")
    current_widgets.append(bad3)
    best = tk.Listbox(curr, font=("Pixeloid Sans", 18),height=8, width=32, border=0, activestyle="none", 
                      bg=green, selectbackground=green)
    best.place(relx=0.37, rely=0.65, anchor="center")
    best.insert(tk.END, firstS)
    best.insert(tk.END, "")
    best.insert(tk.END, secondS)
    best.insert(tk.END, "")
    best.insert(tk.END, thirdS)
    current_widgets.append(best)
    worst = tk.Listbox(curr, font=("Pixeloid Sans", 18),height=8, width=32, border=0, activestyle="none", 
                       bg=green, selectbackground=green)
    worst.place(relx=0.64, rely=0.65, anchor="center")
    worst.insert(tk.END, worst1)
    worst.insert(tk.END, "")
    worst.insert(tk.END, worst2)
    worst.insert(tk.END, "")
    worst.insert(tk.END, worst3)
    current_widgets.append(worst)

def per_pack_pokemon(curr, userlist, packlist):
    #get all match vecs
    #when user clicks on pack, that matchvec will appear on opposite side
    list_of_matches = []
    curr_matches = []
    for list in packlist:
        for i in userlist:
            for pkm in list:
                if i == pkm:
                    curr_matches.append(pkm)
        list_of_matches.append(curr_matches)
        curr_matches = []
    pack_lst = tk.Listbox(curr, font=("Pixeloid Sans", 20),height=15, width=20, border=0, activestyle="none", bg=highlight, 
                     selectbackground="#94b17b")
    pack_lst.place(relx=0.37, rely=0.65, anchor="center")
    update(pack_lst, packnames)
    current_widgets.append(pack_lst)

    pkm_lst = tk.Listbox(curr, font=("Pixeloid Sans", 20),height=15, width=20, border=0, activestyle="none", bg=highlight, 
                         selectbackground="#94b17b")
    pkm_lst.place(relx=0.62, rely=0.65, anchor="center")
    current_widgets.append(pkm_lst)

    collect = tk.Label(curr, text="Pokémon per Pack", bg=green, font = ("Pixeloid Sans", 20))
    collect.place(relx=0.5, rely=0.38, anchor="center")
    current_widgets.append(collect)

    info = tk.Label(curr, text="Double click pack to see Pokémon available for that pack.", bg=green, font = ("Pixeloid Sans", 12))
    info.place(relx=0.5, rely=0.42, anchor="center")
    current_widgets.append(info)

    def get_matches(e):
        pack = pack_lst.curselection()
        pack = packnames[pack[0]]
        list_to_use = []
        pkm_lst.delete(0, tk.END)
        for i in range(len(packnames)):
            if packnames[i] == pack:
                list_to_use = list_of_matches[i]
        for pkm in list_to_use:
            pkm_lst.insert(tk.END, pkm)

    pack_lst.bind("<Double-1>", get_matches)

def delete_pokemon(curr, userlist, packlist):
    search_bar = tk.Entry(curr, font=("Pixeloid Sans", 20), bg=highlight, bd=0, borderwidth=0.01)
    search_bar.place(relx=0.5, rely=0.4, anchor="center")
    current_widgets.append(search_bar)
    search_bar.insert(0, "Search...")

    def del_text(event):
        search_bar.delete(0, tk.END)
    
    search_bar.bind("<FocusIn>", del_text)
    lst = tk.Listbox(curr, font=("Pixeloid Sans", 20),height=15, width=20, border=0, activestyle="none", bg=highlight, 
                     selectbackground="#94b17b")
    lst.place(relx=0.37, rely=0.65, anchor="center")
    current_widgets.append(lst)
    update(lst, userlist)

    del_lst = tk.Listbox(curr, font=("Pixeloid Sans", 20),height=15, width=20, border=0, activestyle="none", bg=highlight, 
                         selectbackground="#94b17b")
    del_lst.place(relx=0.62, rely=0.65, anchor="center")
    current_widgets.append(del_lst)
    list_data[:] = userlist

    info = tk.Label(curr, text="Double click Pokémon to add to deletion list.", bg=green, font = ("Pixeloid Sans", 12))
    info.place(relx=0.5, rely=0.43, anchor="center")
    current_widgets.append(info)

    def check(event):
        typed = search_bar.get()
        if typed == '':
            list_data[:] = userlist
        else:
            list_data[:] = []
            for x in userlist:
                if typed.lower() in x.lower():
                    list_data.append(x)
        update(lst, list_data)
    
    list_to_delete = []
    def add_to_delete_list(event):
        found = False
        choice = lst.curselection()
        for pokemon in list_to_delete:
            if pokemon == list_data[choice[0]]:
                found = True
        if not found:
            list_to_delete.append(list_data[choice[0]])
            del_lst.insert(0, list_data[choice[0]])
    
    def remove_from_list(event):
        choice = del_lst.curselection()
        for pokemon in list_data:
            if pokemon == list_data[choice[0]]:
                list_data.remove(pokemon)
    def delete_from_list(curr, userlist, removelist):
        for x in removelist:
            if x in userlist:
                userlist.remove(x)
        del_lst.delete(0, tk.END)
        update(lst, userlist)
        for x in removelist:
            users.delete_pokemon(x, sys_user)

        
    del_button = tkm.Button(curr, font=("Pixeloid Sans", 12), bg=highlight, 
                        height=40, width=120, text="Delete Pokémon", bordercolor=green, borderwidth=0, relief=tk.SUNKEN,
                        activebackground="#94b17b", focuscolor="#94b17b", 
                        command=lambda: delete_from_list(curr, userlist, list_to_delete))
    del_button.place(relx=0.718, rely=0.4, anchor="e")
    current_widgets.append(del_button)

    del_lst.bind("<Double-1>", remove_from_list)
    lst.bind("<Double-1>", add_to_delete_list)
    search_bar.bind("<KeyRelease>", check)

def display_list(curr, userlist, packlist):
    pokemon_list = tk.StringVar(value=userlist)
    collect = tk.Label(curr, text="Pokémon left to collect: " + str(len(userlist)), bg=green)
    collect.configure(font = ("Pixeloid Sans", 20))
    collect.place(relx=0.5, rely=0.4, anchor="center")
    current_widgets.append(collect)

    lst = tk.Listbox(curr,font=("Pixeloid Sans", 20),height=16, width=45,listvariable=pokemon_list, border=0, 
                     bg=green, activestyle="none", selectbackground=highlight)
    lst.place(relx=0.5, rely=0.65, anchor="center")
    current_widgets.append(lst)

def best_pack_list(curr, userlist, packlist):
    bestmatch = 0
    for key in pack_dict:
        if pack_dict[key] > bestmatch:
            bestmatch = pack_dict[key]
            bestpack = key
    bestpack_out = tk.Label(curr, bg=green, text="Best Pack: " + bestpack + " with " + str(bestmatch) + " matches.")
    bestpack_out.configure(font = ("Pixeloid Sans", 20))
    bestpack_out.place(relx=0.5, rely=0.4, anchor="center")
    all = tk.Label(curr, bg=green, text="All packs:")
    all.configure(font = ("Pixeloid Sans", 18))
    all.place(relx=0.5, rely=0.45, anchor="center")
    current_widgets.append(all)
    current_widgets.append(bestpack_out)
    lst = tk.Listbox(curr,font=("Pixeloid Sans", 18),height=15, width=35, border=0, bg=green, activestyle="none", 
                     selectbackground=green)
    lst.place(relx=0.5, rely=0.68, anchor="center")
    current_widgets.append(lst)
    for key in pack_dict:
        addstr = key + ": " + str(pack_dict[key]) + " matches."
        lst.insert(tk.END, addstr)


def window_setup(main_window, username, userlist):
    global sys_user
    sys_user = username
    packlist[:] = users.get_files_from_directory()
    packnames[:] = users.get_pack_names()
    packnames[:] = sorted(packnames[:])
    dict_setup(packlist, userlist)
    font_pkm_title = ("Pixeloid Sans", 30)
    font_pkm_sub = ("Pixeloid Sans", 15)

    user = tk.Toplevel(bg="#9f0720")
    user.title("Pokémon Card Tracker")
    user.attributes('-fullscreen',True)

    path = './assets/pokedex.png'
    pokedex = ImageTk.PhotoImage(Image.open(path).resize((1400, 700)))
    pokedex_img = tk.Label(user, bg="#9f0720")
    pokedex_img.image = pokedex
    pokedex_img.configure(image=pokedex)
    pokedex_img.place(x=20, y=200)

    tkm.Button(user, bg=green, height=40, width=90, borderless=True, font=("Pixeloid Sans", 12), text = "Back to\nUser Select",
               activebackground="#94b17b", focuscolor="#94b17b", command=lambda : close_window(user, main_window)).pack(anchor=tk.NW)
    welcome = tk.Label(user, bg="#9f0720", text="Welcome back, " + username + "!", fg="#ffffff")
    welcome.configure(font = font_pkm_title)
    welcome.pack(side = tk.TOP)

    usage_msg = tk.Label(user, text="Select an action below.", bg="#9f0720", fg="#ffffff")
    usage_msg.config(font = font_pkm_sub)
    usage_msg.pack(side = tk.TOP)

    buttons = tk.Frame(user, height=100, bg="#9f0720")
    buttons.pack()
    b1 = tkm.Button(buttons, font=("Pixeloid Sans", 15), borderless=True, bg=green, height=80, width=250, 
                    text="Display List of Pokémon", activebackground="#94b17b", focuscolor="#94b17b",
                    command=lambda: handler(display_list, user, userlist, packlist)).pack(side=tk.LEFT, padx=5, pady=10, anchor=tk.N)
    b2 = tkm.Button(buttons, font=("Pixeloid Sans", 15), borderless=True, bg=green, height=80, width=250, 
                    text="Find Best Pack Match", activebackground="#94b17b", focuscolor="#94b17b",
                    command=lambda: handler(best_pack_list, user, userlist, packlist)).pack(side=tk.LEFT, padx=5, pady=10,anchor=tk.N)
    b3 = tkm.Button(buttons, font=("Pixeloid Sans", 15), borderless=True, bg=green, height=80, width=250, 
                    text="Top 3 Best and\nWorst Packs", activebackground="#94b17b", focuscolor="#94b17b",
                    command=lambda: handler(tiered_list, user, userlist, packlist)).pack(side=tk.LEFT, padx=5, pady=10,anchor=tk.N)
    b4 = tkm.Button(buttons, font=("Pixeloid Sans", 15), borderless=True, bg=green, height=80, width=250, 
                    text="Delete Pokémon\nfrom User List", activebackground="#94b17b", focuscolor="#94b17b",
                    command=lambda: handler(delete_pokemon, user, userlist, packlist)).pack(side=tk.LEFT, padx=5, pady=10,anchor=tk.N)
    b5 = tkm.Button(buttons, font=("Pixeloid Sans", 15), borderless=True, bg=green, height=80, width=250,
                    text="Find Pokémon per Pack", activebackground="#94b17b", focuscolor="#94b17b",
                    command=lambda: handler(per_pack_pokemon, user, userlist, packlist)).pack(side=tk.LEFT, padx=5, pady=10, anchor=tk.N)

    ##### ACTION BUTTONS #####
    #1. find best pack match
    #2. find pokemon in specific pack
    #3. get number of pokemon left to collect
    #4. find top three best/worst packs
    #5. find matches given a specific pack
    
    user.bind('<Escape>',close_prog)
    user.deiconify()
    #time.sleep(0.5)
    main_window.iconify()
