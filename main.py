import os
import sys


def yesnoquitopen(word):
    if word == "Yes" or word == "yes" or word == "Y" or word == "y":
        return 0
    elif word == "No" or word == "no" or word == "N" or word == "n":
        return 1
    elif word == "Open" or word == "open" or word == "O" or word == "o":
        return 2
    elif word == "Quit" or word == "quit" or word == "Q" or word == "q":
        goodbye("Quitting by user request...")
    else:
        return -1


def goodbye(code):
    print(code)
    sys.exit(0)


if __name__ == '__main__':
    confirm = -1
    file_path = None
    print("Welcome to the file cleaner! Follow the prompts to clean your files. Type 'quit' at any time to exit.")

    while confirm != 0:
        confirm = -1
        print("Write the absolute file path of the folder you'd like to clean:")
        file_path = input()
        if file_path == "Quit" or file_path == "quit" or file_path == "Q" or file_path == "q":
            goodbye("Quitting by user request...")

        while confirm == -1:
            confirm = yesnoquitopen(input("Is " + file_path + " correct? Y/N: "))
            if confirm == 1:
                print("Please type a correct file path or quit.")
            elif confirm == -1:
                print("Please enter yes (Yes, yes, Y, y) or no (No, no, N, n).")
            elif confirm == 0:
                if not os.path.exists(file_path):
                    print("This file path doesn't seem to exist. Please type a correct file path or quit.")
                    confirm = 1

    file_list = None
    try:
        file_list = os.listdir(file_path)
    except:
        goodbye("Something went wrong with identifying the files in your folder. Quitting...")

    print("Looking through your files...")
    print("While we go through your files, you may type 'open' or 'o' at any time to open a file and view it.")
    i = 0
    while i < len(file_list):
        file = file_list[i]
        answer = yesnoquitopen(input("Would you like to delete " + file + "? Y/N/O/Q: "))

        if answer == 0:
            os.remove(file_path + "/" + file)
            print(file + " removed.\n")
            i += 1
        elif answer == 1:
            print("File kept.\n")
            i += 1
        elif answer == 2:
            os.startfile(file_path + "/" + file)
        else:
            print("Please enter: yes (Yes, yes, Y, y) or no (No, no, N, n).\n")
