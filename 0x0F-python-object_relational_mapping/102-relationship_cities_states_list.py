#!/usr/bin/python3
"""Prints all State objects and corresponding city
objects in our db"""

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
    Session = sessionmaker(bind=engine)
    session = Session()

    query_res = session.query(City).all()
    for city in query_res:
        print("{}: {} -> {}".format(city.id, city.name,
                                    session.query(State).filter(
                                        State.id ==
                                        city.state_id).first().name))
    session.close()
