#!/usr/bin/python3
"""updates an instance in the database
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

    state = session.query(State).filter(State.id == 2).first()
    setattr(state, 'name', "New Mexico")
    session.commit()
    session.close()
