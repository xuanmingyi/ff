from pybrctl import BridgeController
import util

class BridgeDriver(object):
    def __init__(self):
        self.brctl = BridgeController()

    def add(self, name, cidr, dhcp=True):
        self.brctl.addbr(name)
        first_address = util.first_address(cidr)
        util.span("ip addr add {} dev {}".format(first_address, name))
        
        dhcp_address = util.second_address(cidr)
        

    def rm(self):
        pass


    def list(self):
        pass
