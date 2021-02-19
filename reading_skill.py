import speech_recognition as sr
import generate_text_paragraph
import difflib
import csv
from colorama import Fore


def test_reading_skill():
    text_paragraph = generate_text_paragraph.generate_text()

    original_text = ""
    print()
    for line in text_paragraph:
        print(line)
        original_text += line
        original_text += " "

    r = sr.Recognizer()
    spoken_text = ""
    tries = 1
    print()
    print(Fore.CYAN + "Read above text loudly")
    print(Fore.RESET)
    while tries == 1:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.4)
                audio2 = r.listen(source2)
                temp_text = r.recognize_google(audio2)
                temp_text = temp_text.lower()
                spoken_text += temp_text
                tries = 0
        except sr.RequestError as e:
            print(Fore.LIGHTRED_EX + "Could not request results; {0}".format(
                e))
            print(Fore.LIGHTRED_EX + "Speak again")
            print(Fore.RESET)
            tries = 1
        except sr.UnknownValueError:
            print(Fore.LIGHTRED_EX + "unknown error occured")
            print(Fore.LIGHTRED_EX + "Speak again")
            print(Fore.RESET)
            tries = 1

    original_text = original_text.replace(".", "")
    original_text = original_text.replace(" ", "")
    original_text = original_text.lower()

    print()
    print(Fore.GREEN + "Spoken Text : {}".format(spoken_text))
    print()

    spoken_text = spoken_text.replace(" ", "")
    spoken_text = spoken_text.lower()

    average = difflib.SequenceMatcher(
        None, original_text, spoken_text
    ).ratio()

    with open("reading_record.csv", 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([average])
    print(Fore.YELLOW + "Result stored succesfully")
    print(Fore.LIGHTCYAN_EX + "Accuracy : {0:.2f} %".format(average * 100))
    print(Fore.RESET)
