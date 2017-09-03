from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from os.path import join
import config

from oslo_config.cfg import CONF


Base = declarative_base()
sqlite_path = join(CONF.config_dir, "ff.db")
engine = create_engine("sqlite:///{}".format(sqlite_path))


Session = sessionmaker(bind=engine)

class Image(Base):
    __tablename__ = "images"

    name = Column(String, primary_key=True)
    path = Column(String)
    size = Column(String)
    status = Column(String)
    md5sum = Column(String)


def create_table():
    Base.metadata.create_all(engine)
