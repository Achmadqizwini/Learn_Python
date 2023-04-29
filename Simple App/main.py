import os

import crud

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("WELCOME TO THIS PROGRAM")
    print("LIBRARY DATABASE")
    print("=======================")

    # check database ada atau tidak
    crud.init_console()

    while (True):

        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("WELCOME TO THIS PROGRAM")
        print("LIBRARY DATABASE")
        print("=======================")

        print("1. Read data")
        print("2. Create data")
        print("3. Update data")
        print("4. Delete data")

        user_option = input("Masukkan opsi: ")

        print("\n=======================\n")

        match user_option:
            case "1": crud.read_console()
            case "2": print("2. Create data")
            case "3": print("3. Update data")
            case "4": print("4. Delete data")
            case _:
                print("Invalid input")

        print("\n===================\n")
        is_done = input("Apakah sudah selesai? (Y/N)")

        if is_done == "Y" or is_done == "y" or is_done == "Yes" or is_done == "YES":
            break

    print("Program ended, Thank you")
