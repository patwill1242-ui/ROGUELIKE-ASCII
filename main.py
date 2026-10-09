import os

run = True
menu = True
play = False
rules = False

HP = 50 
ATK = 3

def draw():
    print("XX--------------------XX")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def save():
    list = [
        name,
        str(HP),
        str(ATK)
    ]
    f= open("load.txt","w")

    for item in list:
        f.write(item + "\n")
    f.close()    

while run:
    while menu:
        clear()
        draw()
        print("1. NEW GAME")
        print("2. LOAD GAME")
        print("3. RULES")
        print("4. QUIT GAME")
        draw()

        if rules:
            print("im the creator of this simple game")
            rules =False
            choice=""
            input(">")
        else:    
            choice = input("#")

        if choice == "1":
            clear()
            name=input("what is your name player? ")
            menu = False
            play = True
        elif choice == "2":
            f = open("load.txt","r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP = load_list[1][-1]
            ATK = load_list[2][-1]
            clear()
            print("Welcome back ",name)
            input(">")
            menu = False
            play = True
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  #autosave

        clear()
        draw()
        print("0. SAVE AND QUIT" )
        draw() 

        dest = input("#")

        if dest == "0":
            play = False 
            menu = True
            save()