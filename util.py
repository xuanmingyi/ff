import random
import string
import subprocess
from prettytable import PrettyTable
from netaddr import IPNetwork


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


def span(command):
    command = command.split()
    child = subprocess.Popen(command, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    child.wait()
    return child.stdout.read(), child.stderr.read()


def first_address(cidr):
    ip_list = filter(lambda x: str(x).split(".")[-1] != '0' and \
        str(x).split(".")[-1]!= '255', list(IPNetwork(cidr)))
    return ip_list[0]


def second_address(cidr):
    ip_list = filter(lambda x: str(x).split(".")[-1] != '0' and \
        str(x).split(".")[-1]!= '255', list(IPNetwork(cidr)))
    return ip_list[1]
