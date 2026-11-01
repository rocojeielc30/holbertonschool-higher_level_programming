#!/usr/bin/python3
"""Deletes all State objects containing the letter a from hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, database):
    """Find every State whose name contains a and delete it."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%")).all()

    for state in states:
        session.delete(state)

    session.commit()

    session.close()


if __name__ == "__main__":
    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])