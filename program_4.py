# Nathan Parker
# 05/02/25
# Program #4

import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a cursor.
    cur = conn.cursor()

    # Get a choice from the user.
    answer = input('''1 – Read Entry
2 – Update Entry
3 – Delete Entry
4 – Add Entry
Enter the number of your choice: ''')

    # While choice is invalid, get another choice.
    while answer != '1' and answer != '2' and answer != '3' and answer != '4':
        print('Invalid Input')
        answer = input('Enter the number of your choice: ')

    # Call the function that corresponds with the chosen option.
    if answer == '1':
        read(cur)
    elif answer == '2':
        update(cur)
    elif answer == '3':
        delete(cur)
    elif answer == '4':
        add(cur)

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()

# Define the read function.
def read(cur):
    # Display the data from the database.
    for row in cur.execute('SELECT * FROM Entries'):
        print(f'{row[0]:<3}{row[1]:20}{row[2]}')

# Define the update function.
def update(cur):
    # Get an ID number from the user.
    id_num = input('Enter an entry ID number: ')

    # Select the data that corresponds to the chosen ID number.
    cur.execute('''SELECT Name, Number FROM Entries
    WHERE EntryID == ?''', (id_num))
    results = cur.fetchone()

    # If the ID was found, continue.
    if results != None:
        # Display the name and number that correspond with the chosen ID.
        print(f"{results[0]}'s current number is {results[1]}.")
        # Get a new number for that ID.
        new_num = input(f'Enter a new number for {results[0]}: ')

        # Update the database with the new number.
        cur.execute('''UPDATE Entries SET Number = ?
        WHERE EntryID == ?''', (new_num, id_num))

        # Display a message saying that the database was updated.
        print(f"{results[0]}'s number was updated to {new_num}.")

    # If the ID was not found, display a message saying so.
    else:
        print(f'{id_num} not found.')

# Define the delete function.
def delete(cur):
    # Get an ID number from the user.
    id_num = input('Enter an entry ID number: ')

    # Select the data that corresponds to the chosen ID number.
    cur.execute('''SELECT Name, Number FROM Entries
        WHERE EntryID == ?''', (id_num))
    results = cur.fetchone()

    # If the ID was found, continue.
    if results != None:
        # Delete the row of the chosen ID from the database.
        cur.execute('''DELETE FROM Entries WHERE EntryID == ?''', (id_num))

        # Display a message saying that the database was updated.
        print(f"{results[0]}'s number was deleted.")

    # If the ID was not found, display a message saying so.
    else:
        print(f'{id_num} not found.')

# Define the add function.
def add(cur):
    # Get a new name from the user.
    name = input('Enter a name: ')

    # Get a new number from the user.
    number = input('Enter a number: ')

    # Insert the name and number into the database.
    cur.execute('''INSERT INTO Entries (Name, Number)
                        VALUES (?, ?)''', (name, number))

    # Display a message saying that the database was updated.
    print(f"{name}'s number was added.")

# Call the main function.
if __name__ == '__main__':
    main()
