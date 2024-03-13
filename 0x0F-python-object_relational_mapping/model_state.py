#!/usr/bin/python3
"""
First states model using sql alchemy
This is first of many
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Model for the state class to help with
    ORM for our project"""

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
