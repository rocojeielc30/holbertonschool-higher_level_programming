#!/usr/bin/python3
"""Lists all State objects containing the letter a from hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_states_with_a(username, password, database):
    """Print every State whose name contains the letter a, sorted by id."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .order_by(State.id)
        .all()
    )

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    filter_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])