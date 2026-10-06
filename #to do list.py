#to do list
import os

menu="""
    0: Close app
    1: Add new task
    2: Show all task
    3: Complete task
    4: Delete task
    5: Delete all task
"""

if os.path.exists("to_do_list.txt") and os.path.getsize("to_do_list.txt") > 0:
        print("File exist, Loading file..")
        print("from: ",os.getcwd())        
else:
    print("Creating file..")
    with open("to_do_list.txt","w") as file:
        file.write("-----TO DO LIST-----\n")

while True:
    

    print(menu)

    while True:
        try:
            op=int(input("Choose the option: "))

            if op in [0,1,2,3,4,5]:
                break
            else:
                print("Choose not valid")

        except ValueError:
            print("Input not valid")

    with open("to_do_list.txt","r") as file:
        all_text = file.readlines()
    
    column_number= len(all_text)
            
    if op == 0:
        break
    elif op == 1:
        with open("to_do_list.txt","a") as file:
            file.write(input("Write the new task: "))
            file.write(" ❌ "+"\n")

    elif op == 2:
        for task in all_text:
            print(task, end="")
    elif op == 3:
        for i, task in enumerate(all_text):
            if i == 0:
                print(task, end="")
            else:
                print(f"[{i}] {task}", end="")
        while True:
                try:
                    complete=int(input("What task would you complete?: "))
                    if complete in range(column_number) and complete != 0:
                        break
                    else:
                        print("Choose not valid")
                except ValueError:
                    print("Input not valid")
        for i, task in enumerate(all_text):
            if i == 0:
                with open("to_do_list.txt","w") as file:
                    file.write("-----TO DO LIST-----\n")
            elif i == complete:
                all_text[i] = all_text[complete].replace("❌","✅")    
                with open("to_do_list.txt","a") as file:
                    file.write(all_text[i]) 
            else:
                with open("to_do_list.txt","a") as file:
                    file.write(all_text[i])
                 
    elif op == 4:
        for i, task in enumerate(all_text):
            if i == 0:
                print(task, end="")
            else:
                print(f"[{i}] {task}", end="")
        while True:
            try:
                delete=int(input("What task would you delete?: "))
                if delete in range(column_number) and delete != 0:
                    break
                else:
                    print("Choose not valid")
            except ValueError:
                    print("Input not valid")
        for i, task in enumerate(all_text):
            if i == 0:
                with open("to_do_list.txt","w") as file:
                    file.write("-----TO DO LIST-----\n")
            elif i != delete:
                with open("to_do_list.txt","a") as file:
                    file.write(all_text[i])
    else:
        with open("to_do_list.txt","w") as file:
            file.write("-----TO DO LIST-----\n")    