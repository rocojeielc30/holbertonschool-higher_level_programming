#!/usr/bin/python3
"""Lists all cities of a given state from the hbtn_0e_4_usa database."""
import sys
import MySQLdb


def filter_cities(username, password, database, state_name):
    """Print the names of all cities in state_name, comma separated."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # Join cities to states, keep only the requested state, safely
    cursor.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = BINARY %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )

    rows = cursor.fetchall()

    # Each row is a one-item tuple like ('Dallas',), so take item 0
    city_names = [row[0] for row in rows]

    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])