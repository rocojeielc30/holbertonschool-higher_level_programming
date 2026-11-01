#!/usr/bin/python3
"""Lists all states from the hbtn_0e_0_usa database, sorted by id."""
import sys
import MySQLdb


def list_states(username, password, database):
    """Connect to MySQL and print every row of the states table by id."""
    # Open a connection to the MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # The cursor is the object that runs queries and holds results
    cursor = db.cursor()

    # Ask MySQL for all states, smallest id first
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Get every resulting row as a tuple of tuples
    rows = cursor.fetchall()

    # Each row looks like (1, 'California'), printed exactly as-is
    for row in rows:
        print(row)

    # Release the cursor and close the connection
    cursor.close()
    db.close()


# Only run when executed directly, not when imported
if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])