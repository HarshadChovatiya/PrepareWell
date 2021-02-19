from pyfiglet import Figlet
import listening_skill
import reading_skill
import writing_skill
import display_performance
from colorama import Fore
import os
import csv


def perform_windup():
    list_of_files = [
        "listening_record.csv",
        "reading_record.csv",
        "writing_record.csv"
    ]

    for i in range(3):
        try:
            os.remove(list_of_files[i])
        except FileNotFoundError:
            pass

    # Code to clear cache
    file_name = "topics.csv"
    fields = ["Topic", "Information"]
    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file, fieldnames=fields)
        data = list(csv_reader)

    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fields)
        csv_writer.writerow({"Topic": "Topic", "Information": "Information"})
        for i in range(1, len(data)):
            row = {"Topic": data[i]["Topic"], "Information": ''}
            csv_writer.writerow(row)


def display_choice():
    print(Fore.RED + "Please make a choice")
    print(Fore.BLUE + "1. For Test Listening Skill")
    print(Fore.BLUE + "2. For Test Reading Skill")
    print(Fore.BLUE + "3. For Test Writing Skill")
    print(Fore.BLUE + "4. For Display Performance")
    print(Fore.BLUE + "5. Exit")
    print(Fore.RESET)


def ask_for_replay():
    print(Fore.LIGHTGREEN_EX + "Want to play again?")

    again = 0
    while True:
        print(Fore.YELLOW + "1. For yes")
        print(Fore.YELLOW + "2. For no")
        try:
            again = int(input(">>> "))
            if again < 1 or again > 2:
                raise ValueError
        except ValueError:
            print(Fore.LIGHTRED_EX + "Make a valid choice")
            print(Fore.RESET)
        else:
            print(Fore.RESET)
            return again


def main():
    f = Figlet(font='slant')
    print(f.renderText('Prepare Well'))

    again = 1
    while again == 1:
        display_choice()
        try:
            print(Fore.YELLOW + "Make a choice")
            choice = int(input(">>> "))
            print(Fore.RESET)
        except ValueError:
            print(Fore.LIGHTRED_EX + "That was not a valid number")
            print(Fore.RESET)
        else:
            if choice == 1:
                listening_skill.test_listening_skill()
                again = ask_for_replay()
            elif choice == 2:
                reading_skill.test_reading_skill()
                again = ask_for_replay()
            elif choice == 3:
                writing_skill.test_writing_skill()
                again = ask_for_replay()
            elif choice == 4:
                display_performance.show_graph()
                again = ask_for_replay()
            elif choice == 5:
                print(Fore.GREEN + "Bye")
                print(Fore.RESET)
                perform_windup()
                exit(0)
            else:
                print(Fore.LIGHTRED_EX + "Please Enter a valid choice")
                print(Fore.RESET)

    if again == 2:
        print(Fore.GREEN + "Bye")
        print(Fore.RESET)
        perform_windup()
        exit(0)


if __name__ == "__main__":
    main()
    print(Fore.RESET)
