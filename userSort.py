import os 
import shutil

#C:/Users/Zachary Budday/Desktop/messy
#C:/Users/Zachary Budday/Desktop/messy2

FOLDER_PATH = input("Print the full path you want to serach: ")


def print_folders():
    for folder in os.listdir(FOLDER_PATH):
        full_path = os.path.join(FOLDER_PATH, folder)
        if os.path.isdir(full_path): #checks to see if it is a directory 
            print(folder)


def print_files():
    for file in os.listdir(FOLDER_PATH):
        full_path = os.path.join(FOLDER_PATH, file)
        if os.path.isfile(full_path): #checks to see if it is a file
            print(file)


def move_files():
    for file in os.listdir(FOLDER_PATH):
        full_file_path = os.path.join(FOLDER_PATH, file)
        
        
        #loops through only files and asks the user if they want to move them
        if os.path.isfile(full_file_path):
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
        


def menu():
    while True:
        choice = input(f"Do you want to \n1. View the files within your folder\n2. View all subfolders in your folder\n3. Sort your files \n4. Quit: ")
    
        if choice == "1":
            print_files()
        elif choice == "2":
            print_folders()
        elif choice == "3":
            move_files()
        elif choice == "4":
            break

menu()