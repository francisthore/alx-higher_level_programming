#!/usr/bin/python3
"""Prints results of states that contain an
'a' in  their name
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

    query_res = session.query(State).filter(State.name.like('%a%'))
    try:
        for res in query_res:
            session.delete(res)
            session.commit()
    except Exception as e:
        print("Error: ", e)
    session.close()
