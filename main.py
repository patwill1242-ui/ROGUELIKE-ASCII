import os, random

run = True
menu = True
play = False
rules = False
win = False

seed = 0
level = 0
rand = 0
number = 1000
even_or_odd = ""
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
        str(rand),
        str(number),
        str(even_or_odd)
    ]
    with open("load.txt", "w") as f:
        for item in data:
            f.write(item + "\n")

def game_choose(number, rand):
    str_rand = str(rand).zfill(4)
    list_rand = list(map(int, str_rand))
    
    print(f"a) + {list_rand[0]}")
    print(f"b) - {list_rand[1]}")
    print(f"c) * {list_rand[2]}")
    print(f"d) / {list_rand[3]}")
            
    print("\nChoose the order of operations to apply to the number (e.g. abcd, dcba)")
    draw()
    order = input().lower().strip()
    
    for char in order:
        if char == 'a':
            number += list_rand[0]
        elif char == 'b':
            number -= list_rand[1]
        elif char == 'c':
            number *= list_rand[2]
        elif char == 'd':
            if list_rand[3] != 0:
                number //= list_rand[3]
            else:
                print("Division by zero skipped!")
    
    return number

def even_or_odd_random():
    return "even" if random.randint(0, 1) == 0 else "odd"  

def win_decision(number, even_or_odd):
    clear()
    draw()
    is_even = (number % 2 == 0)
    print(f"\nFinal result: {number}")
    if (even_or_odd == "even" and is_even) or (even_or_odd == "odd" and not is_even): 
        print(">>> YOU WIN! <<<\n")
        draw()
        input(">")
        return True
    else:
        print(">>> YOU LOSE! <<<\n")
        draw()
        input(">")
        return False
        
def print_title():
    print(r"""
______ _____ _____ _   _ _____ ___  ___  ___ _____ _   _ 
| ___ \  _  |  __ \ | | |  ___|  \/  | / _ \_   _| | | |
| |_/ / | | | |  \/ | | | |__ | .  . |/ /_\ \| | | |_| |
|    /| | | | | __| | | |  __|| |\/| ||  _  || | |  _  |
| |\ \\ \_/ / \__/\ |_| | |___| |  | || | | || | | | | |
\_| \_|\___/ \____/\___/\____/\_|  |_/\_| |_/\_/ \_| |_/
    """)    
    print("                             Made by Patricks Williams")

clear()
print_title()
input("\n\n>")
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
            print("Rules:")
            print("- Order the operations (a, b, c, d) to reach an Even or Odd number.")
            print("- a: Adds 1st digit")
            print("- b: Subtracts 2nd digit")
            print("- c: Multiplies by 3rd digit")
            print("- d: Divides by 4th digit")
            rules = False
            choice = ""
            input("\nPress enter to go back...")
        else:    
            choice = input("#")

        if choice == "1":
            clear()
            name = input("What is your name player? ")
            op = input("Do you have a seed? ").strip().lower()
            
            if op == "yes":
                valid = False
                while not valid:
                    try:
                        seed_input = int(input("Insert a 5-digit seed: "))
                        if seed_input > 0 and seed_input % 10 != 0 and len(str(seed_input)) == 5:
                            seed = seed_input
                            valid = True
                        else:
                            print("Seed not valid")
                    except ValueError:
                        print("Insert a valid number")
            else:
                seed = random.randint(10000, 99999)
                while seed % 10 == 0:
                    seed = random.randint(10000, 99999)
            
            level = 0
            number = 1000
            rand = seed
            menu = False
            play = True
            
        elif choice == "2":
            try:
                with open("load.txt", "r") as f:
                    load_list = f.readlines()
                
                if len(load_list) >= 6:
                    name = load_list[0].strip()
                    seed = int(load_list[1].strip())
                    level = int(load_list[2].strip())
                    rand = int(load_list[3].strip())
                    number = int(load_list[4].strip())
                    even_or_odd = load_list[5].strip()
                    clear()
                    print("Welcome back ", name)
                    input(">")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file")
                    input(">")
            except (OSError, ValueError):
                print("No loadable save file")
                input(">")

        elif choice == "3":
            rules = True

        elif choice == "4":
            clear()
            print("Thanks for playing!")
            exit()

    while play:
        clear()
        draw()
        print("0. SAVE AND QUIT")
        print("1. NEXT LEVEL")
        draw() 

        dest = input("#")

        if dest == "0":
            save()
            play = False 
            menu = True

        elif dest == "1":
            clear()
            level += 1
            draw()
            print("LEVEL ", level)
            even_or_odd = even_or_odd_random()
            print("Target:", even_or_odd.upper())
            
            if level == 1:
                rand = int(str(seed)[1:5])
            else:
                temp = str(rand ** 2).zfill(8)
                rand = int(temp[2:6])

            print("n:", number)
            number = game_choose(number, rand)
            win = win_decision(number, even_or_odd)
            if win == False:
                play = False 
                menu = True
            