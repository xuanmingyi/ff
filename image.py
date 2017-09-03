from base import Core
import models
import os
import shutil
import util
import hashlib
from oslo_config.cfg import CONF


class Image(Core):
    subcommand = "image"
    
    def add(self, filepath, name):
        filename = filepath.split("/")[-1]
        statinfo = os.stat(filepath)
        size = util.convert_size(statinfo.st_size)
        with open(filepath) as f:
            md5sum = hashlib.md5(f.read()).hexdigest()
        destname = os.path.join(CONF.config_dir, "images", md5sum)
        shutil.copyfile(filepath, destname)
        image = models.Image(name=name,
                             path=destname,
                             size=size,
                             status="available",
                             md5sum=md5sum)
        self.session.add(image)
        self.session.commit()

 
    def rm(self, name):
        image = self.session.query(models.Image)\
            .filter_by(name=name, status="available").first()
        image.status = "deleted"
        self.session.commit()


    def list(self):
        images = self.session.query(models.Image)\
            .filter_by(status="available")
        util.print_table(["name", "size", "status"],
            map(lambda x: [x.name, x.size, x.status], images))
