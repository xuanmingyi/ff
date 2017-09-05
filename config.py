from oslo_config import cfg
from oslo_config import types

from os.path import expanduser

opts = [
    cfg.StrOpt("config_dir",
               default=expanduser("~/.ff")),
    cfg.StrOpt("network_driver",
               default="bridge")
]


CONF = cfg.CONF
CONF.register_opts(opts)
