#!/usr/bin/python3
"""Prints all City objects from our db"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    db_user = argv[1]
    db_pwd = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        db_user, db_pwd, "localhost", db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_add = State(name="California")
    city_add = City(name="San Francisco", state=state_add)
    session.add(state_add)
    session.add(city_add)
    session.commit()
    session.close()
