from sqlalchemy import Sequence, Column, Integer, String
from geoalchemy2 import Geometry
from SQL_db_params import *
from cords_functions import *

### KLASY ###

### PRACOWNICY ###
class Worker(Base):
    __tablename__ = 'workers_list'

    id = Column(Integer(), Sequence('worker_id_seq'), primary_key=True)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=False)
    function = Column(String(100), nullable=False)
    id_workplace = Column(String(), nullable=False)

    def __init__(self, name, lastname, city, function, id_workplace):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.function = function
        self.id_workplace = id_workplace
        cordy = get_cordinates(city)
        self.location = f'POINT({cordy[1]} {cordy[0]})'


### ODDZIAŁY ###
class Workplace(Base):
    __tablename__ = 'workplace_list'

    id = Column(Integer(), Sequence('workplace_id_seq'), primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    id_workplace = Column(String(), nullable=False)

    def __init__(self, name, city, country, id_workplace):
        self.name = name
        self.city = city
        self.country = country
        self.id_workplace = id_workplace
        cordy = get_cordinates(city)
        self.location = f'POINT({cordy[1]} {cordy[0]})'

Base.metadata.create_all(engine)