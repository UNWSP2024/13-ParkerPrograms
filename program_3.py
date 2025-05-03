# Nathan Parker
# 05/02/25
# Program #3

import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a cursor.
    cur = conn.cursor()

    # Create a table if it does not exist.
    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (EntryID INTEGER PRIMARY KEY NOT NULL, 
    Name TEXT, Number TEXT)''')

    # Create a list to hold data that will be added to the database.
    names_and_numbers = [(1, 'George Washington', '111-111-1111'),
                         (2, 'John Adams', '222-222-2222'),
                         (3, 'Thomas Jefferson', '333-333-3333'),
                         (4, 'James Madison', '444-444-4444'),
                         (5, 'James Monroe', '555-555-5555')]

    # Add the data in the list to the database.
    for row in names_and_numbers:
        cur.execute('''INSERT INTO Entries (EntryID, Name, Number)
                    VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()

# Call the main function.
if __name__ == '__main__':
    main()
