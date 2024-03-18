#!/usr/bin/python3
"""Adds an instance to the database
"""

from model_state import State, Base
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

    new_state = State()
    new_state.name = 'Louisiana'
    session.add(new_state)
    session.commit()
    query_res = session.query(State).filter(
        State.name.like('Louisiana')).first()
    if query_res:
        print(query_res.id)
    session.close()
