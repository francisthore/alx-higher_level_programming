#!/usr/bin/python3
"""Prints all City objects from our db"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    db_user = argv[1]
    db_pwd = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        db_user, db_pwd, "localhost", db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    query_res = session.query(City, State).filter(City.state_id == State.id).all()
    print(query_res)
