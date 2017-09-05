from base import Core

import config
import util

from oslo_config.cfg import CONF
import models


from drivers.bridge import BridgeDriver
from drivers.ovs import OVSDriver

DRIVERS = {
    "bridge": BridgeDriver,
    "ovs": OVSDriver
}

class Network(Core):
    def __init__(self):
        super(Network, self).__init__()
        self.driver = DRIVERS[CONF.network_driver]()

    def add(self, name, cird, dhcp=True):
        self.driver.add(name, cird, dhcp=dhcp)
        network = models.Network(name=name,
                                 cird=cird,
                                 dhcp=dhcp,
                                 driver=CONF.network_driver)
        self.session.add(network)
        self.session.commit() 


    def rm(self):
        pass

    def list(self):
        networks = self.session.query(models.Network).all()
        util.print_table(["name", "cird", "dhcp","type"],
            map(lambda x: [x.name, x.cird, x.dhcp, x.driver], networks))
