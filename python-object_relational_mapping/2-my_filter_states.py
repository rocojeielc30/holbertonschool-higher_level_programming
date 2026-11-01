#!/usr/bin/python3
"""Displays all states from hbtn_0e_0_usa whose name matches an argument."""
import sys
import MySQLdb


def my_filter_states(username, password, database, state_name):
    """Print every state whose name exactly matches state_name, by id."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # The user input is placed into the query with format, as required
    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY states.id ASC"
    ).format(state_name)

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    my_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])