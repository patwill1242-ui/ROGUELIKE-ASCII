import os, random

run = True
menu = True
play = False
rules = False

seed = 0
level = 0
rand = 0
name = ""

def draw():
    print("XX--------------------XX")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def save():
    data = [
        name,
        str(seed),
        str(level),
        str(rand)
    ]
    with open("load.txt", "w") as f:
        for item in data:
            f.write(item + "\n")

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
            rules = False
            choice = ""
            input(">")
        else:    
            choice = input("#")

        if choice == "1":
            clear()
            name = input("what is your name player? ")
            op = input("did you have a seed? ").strip().lower()
            
            if op == "yes":
                valid = False
                while not valid:
                    try:
                        seed_input = int(input("insert seed: "))
                        if seed_input % 10 != 0 and len(str(abs(seed_input))) == 5:
                            seed = seed_input
                            valid = True
                        else:
                            print("seed not valid")
                    except ValueError:
                        print("insert a valid number")
            else:
                seed = random.randint(10000, 99999)
                while seed % 10 == 0:
                    seed = random.randint(10000, 99999)
            
            level = 0
            rand = seed
            menu = False
            play = True
            
        elif choice == "2":
            try:
                with open("load.txt", "r") as f:
                    load_list = f.readlines()
                
                if len(load_list) >= 4:
                    name = load_list[0].strip()
                    seed = int(load_list[1].strip())
                    level = int(load_list[2].strip())
                    rand = int(load_list[3].strip())
                    
                    clear()
                    print("Welcome back ", name)
                    input(">")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file")
                    input(">")
            except (OSError, ValueError):
                print("No loadble save file")
                input(">")

        elif choice == "3":
            rules = True

        elif choice == "4":
            exit()

    while play:
        save()

        clear()
        draw()
        print("0. SAVE AND QUIT")
        print("1. NEXT LEVEL")
        draw() 

        dest = input("#")

        if dest == "0":
            play = False 
            menu = True

        elif dest == "1":
            clear()
            level += 1
            draw()
            print("LEVEL ", level)
            
            if level == 1:
                rand = seed
            else:
                temp = str(rand ** 2).zfill(8)
                rand = int(temp[2:6])
                
            print("n:", rand)
            draw()
            input(">")