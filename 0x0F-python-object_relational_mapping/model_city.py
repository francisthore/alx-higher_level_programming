#!/usr/bin/python3
"""This model defines a city"""

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """This class is a model for a city"""
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states"), nullable=False)
