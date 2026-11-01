#!/usr/bin/python3
"""Lists all states starting with an uppercase N from hbtn_0e_0_usa."""
import sys
import MySQLdb


def filter_states(username, password, database):
    """Print every state whose name starts with uppercase N, sorted by id."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # BINARY makes the match case-sensitive, so lowercase n is excluded
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY states.id ASC"
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])