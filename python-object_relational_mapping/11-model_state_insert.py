#!/usr/bin/python3
"""Adds the State object Louisiana to the hbtn_0e_6_usa database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_louisiana(username, password, database):
    """Create a Louisiana State, save it, and print its new id."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == "__main__":
    insert_louisiana(sys.argv[1], sys.argv[2], sys.argv[3])