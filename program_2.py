from os import stat_result

command = ""
print_result = ""
start_result = "Car started...Ready to go!"
stop_result = "Car stopped!"
start_warning = "You have already started the car!"
stop_warning = "You have stopped the car!"
help_result = """
start - starts the car
stop - stops the car
quit - exits the program
"""

while True:
    command = input("> ")
    if command == "start":
        print_result = start_result if start_result !=print_result\
            and print_result != start_warning\
            else start_warning
        print(print_result)
    elif command == "stop":
        print_result = stop_result if stop_result != print_result \
            and print_result != stop_warning \
            else stop_warning
        print(print_result)
    elif command == "help":
        print_result = help_result
        print(print_result)
    elif command == "quit":
        break
    else: print("I don't understand you")