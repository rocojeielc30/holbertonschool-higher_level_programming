#!/usr/bin/python3
"""Safely displays states from hbtn_0e_0_usa whose name matches an argument."""
import sys
import MySQLdb


def my_safe_filter_states(username, password, database, state_name):
    """Print every state whose name matches state_name, safe from injection."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # %s is a placeholder that MySQLdb fills in and escapes safely
    query = (
        "SELECT * FROM states "
        "WHERE name = BINARY %s "
        "ORDER BY states.id ASC"
    )

    # The value is passed separately, inside a tuple
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])