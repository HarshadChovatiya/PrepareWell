import generate_text_paragraph
import difflib
import csv
from colorama import Fore
import time
import pyperclip


def test_writing_skill():
    list_of_text = generate_text_paragraph.generate_text()

    original_text = ""
    print()
    for line in list_of_text:
        print(line)
        original_text += line
        original_text += " "
    print()
    print(Fore.CYAN + "Type above text in a 120 seconds")
    print(
        Fore.LIGHTRED_EX +
        "Copy and paste of a character/word result into zero accuracy"
    )
    print(Fore.RESET)

    written_line = ""
    pyperclip.copy("")
    start_time = time.perf_counter()
    for _ in range(len(list_of_text)):
        written_line += input(">>> ")
        written_line += " "

    end_time = time.perf_counter()
    delay = (end_time - start_time) - 120
    average = difflib.SequenceMatcher(
            None, original_text, written_line).ratio()

    if delay >= 1.00 and delay <= 15.00:
        average -= 0.03
    elif delay > 15.00 and delay <= 30.00:
        average -= 0.06
    elif delay > 30.00:
        average -= 0.1

    test_empty_text = written_line.replace(" ", "")
    if average <= 0.00 or len(test_empty_text) == 0:
        average = 0
    elif len(pyperclip.paste()) != 0:
        average = 0
        print()
        print(Fore.LIGHTRED_EX + "You copied the text")

    print()
    print(Fore.CYAN + "Total time taken : {0:.2f} seconds".format(
        (end_time - start_time)
    ))
    if delay > 0:
        print()
        print(Fore.LIGHTRED_EX + "Delay of {0:.2f} second".format(
            delay
        ))
    print(Fore.RESET)
    with open("writing_record.csv", 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([average])
    print(Fore.YELLOW + "Result stored succesfully")
    print(Fore.LIGHTCYAN_EX + "Accuracy : {0:.2f} %".format(average * 100))
    print(Fore.RESET)
