import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


    ### PARAMETRY POŁĄCZENIA ###

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='123',
    host='localhost',
    database='postgres',
    port=5433)


    ### ŁĄCZENIE Z SQL ###

engine = create_engine(db_params)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
