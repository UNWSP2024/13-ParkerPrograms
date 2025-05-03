# Nathan Parker
# 05/02/25
# Program #2

import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('cities.db')

    # Get a cursor.
    cur = conn.cursor()

    # Display a title for the data.
    print(f'{'':<7}City{'':<16}Population')
    print('—————————————————————————————————————')

    # Display the information from the database.
    cur.execute('SELECT * FROM Cities')
    data = cur.fetchall()
    for row in data:
        print(f'{row[0]:<4}–  {row[1]:20}{row[2]:,.0f}')

    # Close the connection.
    conn.close()

# Call the main function.
if __name__ == '__main__':
    main()
