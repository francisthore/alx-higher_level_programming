#!/usr/bin/python3
"""
Testing the model by creating table
"""
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://mamba:   @localhost/hbtn_0e_6_usa')
    Base.metadata.create_all(engine)
