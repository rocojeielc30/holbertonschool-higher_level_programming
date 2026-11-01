#!/usr/bin/python3
"""Lists all cities from hbtn_0e_4_usa together with their state names."""
import sys
import MySQLdb


def cities_by_state(username, password, database):
    """Print every city with its id, name and state name, sorted by id."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # One query joins cities to states so each city gets its state name
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])