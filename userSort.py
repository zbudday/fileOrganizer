import os 
import shutil

#C:/Users/Zachary Budday/Desktop/messy
#C:/Users/Zachary Budday/Desktop/messy2

FOLDER_PATH = input("Print the full path you want to search: ")
if not os.path.exists(FOLDER_PATH):
    print("The path you typed in does not exist... exiting")
    quit()
            

def buffer_call():
    input("Press Enter to continue... ")


def print_folders():
    for root, dirs, files in os.walk(FOLDER_PATH):
        for folder in dirs:
            full_path = os.path.join(root, folder)
            if os.path.isdir(full_path): #checks to see if it is a directory 
                print(folder)


def print_files():
    for root, dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.isfile(full_path): #checks to see if it is a file
                print(file)


def move_files():
    for root, dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            full_file_path = os.path.join(root, file)
        
            user_input = input(f"Do you want to move {full_file_path}: \n1.Yes \n2.No")

            #if user wants to move it
            if user_input == "1":
                for folder in os.listdir(FOLDER_PATH):
                    full_folder_path = os.path.join(FOLDER_PATH, folder)
                    if os.path.isdir(full_folder_path):
                        print(folder)

                move_to_folder = input("What folder would you like to move it into (enter a name to create a folder) ")

                os.makedirs(os.path.join(FOLDER_PATH, move_to_folder), exist_ok=True)
                shutil.move(full_file_path, os.path.join(FOLDER_PATH, move_to_folder, file))

            #continues if they do not
            elif user_input == "2":
                continue
            
            #invalid option
            else:
                print("not a valid option")
        

def del_empty():
    for root, dirs, files in os.walk(FOLDER_PATH, topdown=False):
        if len(dirs) == 0 and len(files) == 0:
            c1 = input(f"{root} is empty, would you like to delete it? \n1.Yes \n2.No")
            if c1 == "1":
                os.rmdir(root)
            elif c1 == "2":
                continue
            else:
                print("Not a valid choice")
            buffer_call()
            
            
        

def menu():
    while True:
        choice = input(f"Do you want to \n1. View the files within your folder\n2. View all subfolders in your folder\n3. Sort your files \n4. Delete empty folders \n5. Quit: ")
    
        if choice == "1":
            print_files()
            buffer_call()
        elif choice == "2":
            print_folders()
            buffer_call()
        elif choice == "3":
            move_files()
            buffer_call()
        elif choice == "4":
            del_empty()
        elif choice == "5":
            break


menu()