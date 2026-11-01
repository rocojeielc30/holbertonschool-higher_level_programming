#!/usr/bin/python3
"""Prints the first State object from the hbtn_0e_6_usa database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state(username, password, database):
    """Print the State with the lowest id, or Nothing if there are none."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    fetch_first_state(sys.argv[1], sys.argv[2], sys.argv[3])