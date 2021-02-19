from gtts import gTTS
from playsound import playsound
import os
import generate_text_paragraph
import csv
import time
import difflib
from colorama import Fore


def write_to_csv_file(record_list):
    with open("listening_record.csv", 'a', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(record_list)


def test_listening_skill():
    print(Fore.RED + "Listen carefully and try to write the same\n")
    list_of_text = generate_text_paragraph.generate_text()
    language = 'en'
    diff = []
    for line in list_of_text:
        myobj = gTTS(text=line, lang=language, slow=False)
        filename = "readtext_{}.mp3".format(time.time())
        myobj.save(filename)
        playsound(filename)
        os.remove(filename)

        print(Fore.CYAN + "Type the recenlty spoken line" + Fore.RESET)
        written_line = input(">>> ")
        written_line = written_line.lower()
        line = line.lower()
        diff.append(difflib.SequenceMatcher(None, line, written_line).ratio())

    average = sum(diff) / len(diff)

    with open("listening_record.csv", 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([average])
    print()
    print(Fore.YELLOW + "Result stored succesfully")
    print(Fore.LIGHTCYAN_EX + "Accuracy : {0:.2f} %".format(average * 100))
    print(Fore.RESET)
