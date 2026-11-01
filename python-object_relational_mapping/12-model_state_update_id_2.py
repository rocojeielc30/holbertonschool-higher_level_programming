#!/usr/bin/python3
"""Changes the name of the State with id 2 to New Mexico in hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_2(username, password, database):
    """Find the State with id 2 and rename it to New Mexico."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if state is not None:
        state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    update_state_2(sys.argv[1], sys.argv[2], sys.argv[3])