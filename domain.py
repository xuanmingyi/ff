import util
import os

class Disk(object):
    pass

class Domain(object):
    def __init__(self):
        self.name = util.random_string()
        self.cpus = 1
        self.memory = 1024
        self.disks = []
        self.working_dir = os.getcwd()

    def get_config(self):
        if os.path.exists(os.path.join(self.working_dir, "config.py")):
            __import__("config")
        else:
            self.gen_config()

    def get_config(self):
        pass

dom=Domain()
dom.get_config()
