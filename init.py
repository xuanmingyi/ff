from os.path import exists, join, expanduser
from os import mkdir


def init():
    path = expanduser(join("~", ".ff"))
    if exists(path):
        print "had inited exit."
        exit(0)
    else:
        mkdir(path)
        mkdir(join(path, "images"))
