import random
import string
from prettytable import PrettyTable

def random_string(len=8):
    return "".join(random.sample(string.lowercase, len))


def convert_size(size):
    units = [" b", " kb", " mb", " gb", " tb"]
    for i in units:
        if size <= 1024:
            return "{}{}".format(round(size, 2), i)
        else:
            size = size / 1024.0
    return "{}{}".format(round(size, 2), units[-1])


def print_table(title, data):
    table = PrettyTable()
    table.field_names = title
    for row in data:
        table.add_row(row)
    print table
