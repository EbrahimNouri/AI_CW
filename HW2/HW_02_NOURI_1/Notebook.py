from HW2.HW_02_NOURI_1.Functions import *

check_notebook_file()
while True:
    try:
        command = input("""
        1. create new note
        2. show all notes
        3. search in notes
        4. remove note
        5. exit program
        """)

        match command:
            case "1":
                create()
            case "2":
                show()
            case "3":
                search()
            case "4":
                remove()
            case "5":
                print("see you later. ;)")
                break
            case _:
                pass

    except Exception as e:
        print(e)