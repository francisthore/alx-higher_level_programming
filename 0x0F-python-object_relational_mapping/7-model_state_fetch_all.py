#!/usr/bin/python3
"""Lists all states from the states table
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password, database_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    query_res = session.query(State).all()
    for res in query_res:
        print("{}: {}".format(res.id, res.name))
    session.close()
