####################
#       EMMA       #
####################
from os import listdir

def __init__():
    return

def read_in_pokemon(file):
    arr = []
    pokemonFromFile = file.readline()
    while pokemonFromFile:
        pokemonFromFile = pokemonFromFile.strip()
        pokemonFromFile = pokemonFromFile.lower()
        arr.append(pokemonFromFile) 
        pokemonFromFile = file.readline()

    return arr

def get_emma():
    file = open('files/users/emma.txt', 'r')

    emma = []

    pokemonFromFile = file.readline()
    while pokemonFromFile:
        pokemonFromFile = pokemonFromFile.strip()
        emma.append(pokemonFromFile) 
        pokemonFromFile = file.readline()

    file.close()
    return emma

####################
#       ALEX       #
####################
def get_alex():
    file = open('files/users/alex.txt', 'r')
    alex = []

    pokemonFromFile = file.readline()
    while pokemonFromFile:
        pokemonFromFile = pokemonFromFile.strip()
        alex.append(pokemonFromFile) 
        pokemonFromFile = file.readline()

    file.close()
    return alex

def delete_pokemon(del_str, user):
    if (user == "Emma"):
        with open("files/users/emma.txt", "r") as fp:
            lines = fp.readlines()

        with open("files/users/emma.txt", "w") as fp:
            for line in lines:
                if line.strip("\n") != del_str:
                    fp.write(line)
    else:
        with open("files/users/alex.txt", "r") as fp:
            lines = fp.readlines()

        with open("files/users/alex.txt", "w") as fp:
            for line in lines:
                if line.strip("\n") != del_str:
                    fp.write(line)

def get_files_from_directory():
    arr = listdir("./files/cardpacks")
    arr = sorted(arr)
    packs = []
    for pack in arr:
        file = open("./files/cardpacks/" + pack, "r", encoding='utf-8-sig')
        packlist = read_in_pokemon(file)
        file.close()
        packs.append(packlist)
    return packs
    
def get_pack_names():
    file = open("./files/packnames.txt", "r", encoding='utf-8-sig')
    names = []
    name = file.readline()
    while name:
        name = name.strip()
        names.append(name) 
        name = file.readline()
    return names
