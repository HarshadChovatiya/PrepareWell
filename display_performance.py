import csv
from matplotlib import pyplot as plt
from colorama import Fore


def show_graph():
    open("listening_record.csv", 'a')
    open("writing_record.csv", 'a')
    open("reading_record.csv", 'a')

    with open("listening_record.csv") as fl:
        csv_reader = csv.reader(fl)
        data = list(csv_reader)

    data = [float(each[0])*100 for each in data]
    x = [i+1 for i in range(len(data))]

    with open("writing_record.csv") as f2:
        csv_reader = csv.reader(f2)
        data1 = list(csv_reader)

    data1 = [float(each[0])*100 for each in data1]
    x1 = [i+1 for i in range(len(data1))]

    with open("reading_record.csv") as f2:
        csv_reader = csv.reader(f2)
        data2 = list(csv_reader)

    data2 = [float(each[0])*100 for each in data2]
    x2 = [i+1 for i in range(len(data2))]

    if len(data) < 2 and len(data1) < 2 and len(data2) < 2:
        print(Fore.RED + """You need to give atleast two test
of any category to see your performance""")
        print(Fore.RESET)
    else:
        plt.plot(x, data)
        plt.plot(x1, data1)
        plt.plot(x2, data2)
        plt.xlabel("Iteration")
        plt.ylabel("Accuracy")
        plt.legend(["Listening performance", "Writing performance",
                    "Reading performance"])
        plt.title("Performance graph")
        plt.show()
