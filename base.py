from models import Session


class Core(object):
    def __init__(self):
        self.session = Session()
