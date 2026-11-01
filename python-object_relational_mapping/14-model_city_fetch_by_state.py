#!/usr/bin/python3
"""Prints all City objects with their state names from hbtn_0e_14_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, database):
    """Print every city as state name: (city id) city name, by city id."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(State, City)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    fetch_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])