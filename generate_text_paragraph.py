import wikipediaapi
import csv
import random
import shutil
from tempfile import NamedTemporaryFile
import re


def generate_text():
    file_name = "topics.csv"
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ["Topic", "Information"]

    wiki_wiki = wikipediaapi.Wikipedia('en')
    with open(file_name, "r") as fl, tempfile:
        csv_reader = csv.DictReader(fl, fieldnames=fields)
        csv_writer = csv.DictWriter(tempfile, fieldnames=fields)
        data = list(csv_reader)
        rows = len(data) - 1
        num = random.randint(1, rows)
        topic_name = data[num]
        page = ''
        for row in data:
            if row["Topic"] == topic_name["Topic"]:
                if row["Information"] != '':
                    page = row["Information"]
                else:
                    page_data = wiki_wiki.page(topic_name["Topic"])
                    page = page_data.summary
                    row['Information'] = page_data.summary
            row = {"Topic": row["Topic"], "Information": row["Information"]}
            csv_writer.writerow(row)

    shutil.move(tempfile.name, file_name)
    page = re.sub(r"\([^()]*\)", "", page)
    text_paragraph = ""
    punctuation = "!@#$%^&*()_-+=}]{[|\\/>,<'\";~`:"

    for char in page:
        if char not in punctuation:
            text_paragraph += char

    list_of_words = text_paragraph.split()
    list_of_string = []

    i = 0
    while i < len(list_of_words) and len(list_of_string) < 5:
        temp_string = " "
        if i + 10 <= len(list_of_words):
            temp_string = temp_string.join(list_of_words[i:i+10])
            i += 10
            list_of_string.append(temp_string)
        else:
            temp_string = temp_string.join(list_of_words[i:])
            list_of_string.append(temp_string)
            break

    return list_of_string
