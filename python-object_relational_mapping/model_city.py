#!/usr/bin/python3
"""Defines the City class mapped to the MySQL cities table."""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """Represents a city stored as one row in the MySQL cities table."""

    __tablename__ = "cities"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)