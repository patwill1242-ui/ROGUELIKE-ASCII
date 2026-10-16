import os
import random
import sys
import itertools

def delete_last_line():
    sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()

def draw():
    print("XX--------------------XX")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def show_rules():
    clear()
    draw()
    print("RULES")
    draw()
    print("1. Your goal is to make the final number EVEN or ODD based on the Target.")
    print("2. You will be given 4 operations mapped to digits from a generated seed.")
    print("3. Enter the order of operations using 'z', 'x', 'c', 'v' (e.g., 'zxcv', 'vcxz').")
    print("   z = (+), x = (-), c = (*), v = (/)")
    print("4. Survive as many levels as you can!")
    draw()
    input("\nPress ENTER to return to the menu...")

def save_game(name, seed, level, rand_val, number, even_or_odd):
    data = [name, str(seed), str(level), str(rand_val), str(number), even_or_odd]
    with open("load.txt", "w") as f:
        for item in data:
            f.write(item + "\n")

def is_level_winnable(number, list_rand, target_type):
    for order in itertools.permutations(['z', 'x', 'c', 'v']):
        temp_n = number
        for char in order:
            if char == 'z':
                temp_n += list_rand[0]
            elif char == 'x':
                temp_n -= list_rand[1]
            elif char == 'c':
                temp_n *= list_rand[2]
            elif char == 'v':
                if list_rand[3] != 0:
                    temp_n //= list_rand[3]
        
        is_even = (temp_n % 2 == 0)
        if (target_type == "even" and is_even) or (target_type == "odd" and not is_even):
            return True
            
    return False

def game_choose(number, rand_val):
    str_rand = str(rand_val).zfill(4)
    list_rand = list(map(int, str_rand))
    
    print(f"z) + {list_rand[0]}")
    print(f"x) - {list_rand[1]}")
    print(f"c) * {list_rand[2]}")
    print(f"v) / {list_rand[3]}")
            
    print("\nChoose the order of operations to apply to the number (e.g. zxcv, vcxz)")
    draw()
    
    
    while True:
        order = input().lower().strip()
        if len(order)==4 and set(order) =={'z','x','c','v'}:
            break
        else:
            delete_last_line()

    for char in order:
        if char == 'z':
            number += list_rand[0]
        elif char == 'x':
            number -= list_rand[1]
        elif char == 'c':
            number *= list_rand[2]
        elif char == 'v':
            if list_rand[3] != 0:
                number //= list_rand[3]
            else:
                print("Division by zero skipped!")
    
    return number

def win_decision(number, target_type, level):
    clear()
    draw()
    is_even = (number % 2 == 0)
    print(f"\nCurrent level: {level}")
    print(f"Final result: {number}")
    
    player_won = (target_type == "even" and is_even) or (target_type == "odd" and not is_even)
    
    if player_won:
        print(">>> YOU WIN! <<<\n")
    else:
        print(">>> YOU LOSE! <<<\n")
        
    draw()
    input(">")
    return player_won

def main():
    clear()
    print_title()
    input("\n\nPress ENTER to start >")
    
    while True:
        clear()
        draw()
        print("1. NEW GAME")
        print("2. LOAD GAME")
        print("3. RULES")
        print("4. QUIT GAME")
        draw()

        choice = input("# ").strip()

        if choice == "1":
            clear()
            name = input("What is your name player? ")
            op = input("Do you have a seed? (yes/no) ").strip().lower()
            
            if op == "yes":
                while True:
                    try:
                        seed_input = int(input("Insert a 5-digit seed: "))
                        if seed_input > 0 and seed_input % 10 != 0 and len(str(seed_input)) == 5:
                            seed = seed_input
                            break
                        else:
                            print("Seed not valid. Must be 5 digits and not end in 0.")
                    except ValueError:
                        print("Insert a valid number.")
            else:
                seed = random.randint(10000, 99999)
                while seed % 10 == 0:
                    seed = random.randint(10000, 99999)
            
            level = 0
            number = 1000
            rand_val = seed
            even_or_odd = ""
            playing = True

        elif choice == "2":
            try:
                with open("load.txt", "r") as f:
                    load_list = [line.strip() for line in f.readlines()]
                
                if len(load_list) >= 6:
                    name = load_list[0]
                    seed = int(load_list[1])
                    level = int(load_list[2])
                    rand_val = int(load_list[3])
                    number = int(load_list[4])
                    even_or_odd = load_list[5]
                    
                    clear()
                    print(f"Welcome back, {name}!")
                    input(">")
                    playing = True
                else:
                    print("No loadable save file.")
                    input(">")
                    continue
            except (OSError, ValueError):
                print("No loadable save file.")
                input(">")
                continue

        elif choice == "3":
            show_rules()
            continue

        elif choice == "4":
            clear()
            print("Thanks for playing!")
            sys.exit()
        else:
            continue

        while playing:
            clear()
            draw()
            print(f"Current level : {level}")
            print("0. SAVE AND QUIT")
            print("1. NEXT LEVEL")
            draw() 

            dest = input("# ").strip()

            if dest == "0":
                save_game(name, seed, level, rand_val, number, even_or_odd)
                playing = False

            elif dest == "1":
                clear()
                level += 1
                even_or_odd = "even" if random.randint(0, 1) == 0 else "odd"
                
                while True:
                    if level == 1:
                        rand_val = int(str(seed)[1:5])
                    else:
                        temp = str(rand_val ** 2).zfill(8)
                        rand_val = int(temp[2:6])

                    str_rand = str(rand_val).zfill(4)
                    list_rand = list(map(int, str_rand))

                    if is_level_winnable(number, list_rand, even_or_odd):
                        break
                    else:
                        rand_val = (rand_val + 1) % 10000

                draw()
                print(f"LEVEL {level}")
                print(f"Target: {even_or_odd.upper()}")
                print(f"n: {number}")

                number = game_choose(number, rand_val)
                won = win_decision(number, even_or_odd, level)
                
                if not won:
                    playing = False
                    if os.path.exists("load.txt"):
                        os.remove("load.txt")

if __name__ == "__main__":
    main()