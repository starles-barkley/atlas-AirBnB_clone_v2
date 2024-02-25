#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('your_database_uri')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()