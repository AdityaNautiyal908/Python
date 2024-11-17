import mysql.connector as myConn
from mysql.connector import Error

# ANSI escape codes for colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'  # Reset to default color

def create_connection():
    try:
        connection = myConn.connect(
            host = "localhost",
            user = "root",
            password = "8979826321luffy"
        )
        if connection.is_connected():
            print(f"{Colors.GREEN}Connection successful!{Colors.RESET}")
            return connection
    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")
        return None
    
def show_databases(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    
    if databases:
        print(f"{Colors.CYAN}\nAvailable Databases:{Colors.RESET}")
        for i, db in enumerate(databases, start=1):
            print(f"{Colors.GREEN}{i}. {db[0]}{Colors.RESET}")
    else:
        print(f"{Colors.RED}No databases found.{Colors.RESET}")
        
def create_database(connection):
    db_name = input(f"{Colors.YELLOW}Enter the name of the new database: {Colors.RESET}").strip()
    
    if db_name:
        try:
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"{Colors.GREEN}Database '{db_name}' created successfully!{Colors.RESET}")
        except Error as e:
            print(f"{Colors.RED}Error: {e}{Colors.RESET}")
    else:
        print(f"{Colors.RED}Please enter a valid database name.{Colors.RESET}")
        
def drop_database(connection):
    db_name = input(f"{Colors.YELLOW}Enter the name of the database to drop: {Colors.RESET}").strip()

    if db_name:
        try:
            cursor = connection.cursor()
            cursor.execute(f"DROP DATABASE {db_name}")
            print(f"{Colors.GREEN}Database '{db_name}' has been dropped successfully!{Colors.RESET}")
        except Error as e:
            print(f"{Colors.RED}Error: {e}{Colors.RESET}")
    else:
        print(f"{Colors.RED}Please enter a valid database name.{Colors.RESET}")
        
def use_database(connection):
    cursor = connection.cursor()
    
    # Get list of databases
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    
    if not databases:
        print(f"{Colors.RED}No databases available to select.{Colors.RESET}")
        return
    
    # Show the list of databases and let the user select
    print(f"{Colors.CYAN}\nSelect a database to use:{Colors.RESET}")
    for i, db in enumerate(databases, start=1):
        print(f"{Colors.GREEN}{i}. {db[0]}{Colors.RESET}")
    
    try:
        # Get user input
        choice = int(input(f"{Colors.YELLOW}Enter the number of the database you want to use: {Colors.RESET}").strip())
        
        # Check if the choice is valid
        if 1 <= choice <= len(databases):
            selected_db = databases[choice - 1][0]
            print(f"{Colors.GREEN}Using database: {selected_db}{Colors.RESET}")
            cursor.execute(f"USE {selected_db}")
        else:
            print(f"{Colors.RED}Invalid choice. Please select a valid number.{Colors.RESET}")
    except ValueError:
        print(f"{Colors.RED}Invalid input. Please enter a number.{Colors.RESET}")

def drop_table(connection):
    try:
        # Show tables in the current database
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        if not tables:
            print(f"{Colors.RED}No tables available in the current database.{Colors.RESET}")
            return

        print(f"{Colors.YELLOW}Available Tables:{Colors.RESET}")
        for i, table in enumerate(tables, 1):
            print(f"{Colors.CYAN}{i}. {table[0]}{Colors.RESET}")

        # Ask the user to select a table to drop
        table_choice = input(f"{Colors.YELLOW}Select a table to drop (1-{len(tables)}): {Colors.RESET}").strip()
        if not table_choice.isdigit() or int(table_choice) < 1 or int(table_choice) > len(tables):
            print(f"{Colors.RED}Invalid choice.{Colors.RESET}")
            return

        selected_table = tables[int(table_choice) - 1][0]
        print(f"{Colors.GREEN}You selected table: {selected_table}{Colors.RESET}")

        # Ask for confirmation before dropping the table
        confirm = input(f"{Colors.YELLOW}Are you sure you want to drop the table '{selected_table}'? This action cannot be undone (y/n): {Colors.RESET}").strip().lower()

        if confirm == 'y':
            cursor.execute(f"DROP TABLE {selected_table}")
            connection.commit()  # Commit the change
            print(f"{Colors.GREEN}Table '{selected_table}' dropped successfully!{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}Table drop operation canceled.{Colors.RESET}")
    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def truncate_table(connection):
    try:
        # Show tables in the current database
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        if not tables:
            print(f"{Colors.RED}No tables available in the current database.{Colors.RESET}")
            return

        print(f"{Colors.YELLOW}Available Tables:{Colors.RESET}")
        for i, table in enumerate(tables, 1):
            print(f"{Colors.CYAN}{i}. {table[0]}{Colors.RESET}")

        # Ask the user to select a table to truncate
        table_choice = input(f"{Colors.YELLOW}Select a table to truncate (1-{len(tables)}): {Colors.RESET}").strip()
        if not table_choice.isdigit() or int(table_choice) < 1 or int(table_choice) > len(tables):
            print(f"{Colors.RED}Invalid choice.{Colors.RESET}")
            return

        selected_table = tables[int(table_choice) - 1][0]
        print(f"{Colors.GREEN}You selected table: {selected_table}{Colors.RESET}")

        # Ask for confirmation before truncating the table
        confirm = input(f"{Colors.YELLOW}Are you sure you want to truncate the table '{selected_table}'? This will delete all data in the table (y/n): {Colors.RESET}").strip().lower()

        if confirm == 'y':
            cursor.execute(f"TRUNCATE TABLE {selected_table}")
            connection.commit()  # Commit the change
            print(f"{Colors.GREEN}Table '{selected_table}' truncated successfully!{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}Table truncate operation canceled.{Colors.RESET}")
    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")
        
def show_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        print(f"{Colors.YELLOW}Tables in the current database:{Colors.RESET}")
        for table in tables:
            print(f"{Colors.CYAN}{table[0]}{Colors.RESET}")
    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def create_table(connection):
    table_name = input(f"{Colors.YELLOW}Enter the name of the new table: {Colors.RESET}").strip()
    if table_name:
        try:
            # Ask how many columns the user wants to add
            num_columns = int(input(f"{Colors.YELLOW}Enter the number of columns: {Colors.RESET}").strip())

            if num_columns <= 0:
                print(f"{Colors.RED}Number of columns should be greater than 0.{Colors.RESET}")
                return

            columns = []
            for i in range(num_columns):
                print(f"\n{Colors.CYAN}Column {i + 1}: {Colors.RESET}")
                
                # Get column name
                column_name = input(f"{Colors.YELLOW}Enter column name: {Colors.RESET}").strip()

                if not column_name:
                    print(f"{Colors.RED}Column name cannot be empty.{Colors.RESET}")
                    return

                # Get column data type
                column_type = input(f"{Colors.YELLOW}Enter the data type for '{column_name}' (e.g., INT, VARCHAR): {Colors.RESET}").strip()

                if not column_type:
                    print(f"{Colors.RED}Data type cannot be empty.{Colors.RESET}")
                    return

                # If the column type is VARCHAR, ask for the length
                if column_type.upper() == 'VARCHAR':
                    length = input(f"{Colors.YELLOW}Enter the length for '{column_name}' (e.g., 255): {Colors.RESET}").strip()
                    if length.isdigit():
                        column_type = f"VARCHAR({length})"
                    else:
                        print(f"{Colors.RED}Please enter a valid number for length.{Colors.RESET}")
                        return

                # Ask if the user wants to add constraints like UNIQUE, NOT NULL, or AUTO_INCREMENT
                constraints = input(f"{Colors.YELLOW}Enter any constraints for '{column_name}' (e.g., NOT NULL, UNIQUE, AUTO_INCREMENT) or leave empty: {Colors.RESET}").strip()

                # Optional: Ask if the column is a foreign key
                if column_type.upper() == 'INT':
                    is_foreign_key = input(f"{Colors.YELLOW}Is '{column_name}' a foreign key? (y/n): {Colors.RESET}").strip().lower()
                    if is_foreign_key == 'y':
                        reference_table = input(f"{Colors.YELLOW}Enter the referenced table for '{column_name}': {Colors.RESET}").strip()
                        reference_column = input(f"{Colors.YELLOW}Enter the referenced column for '{column_name}': {Colors.RESET}").strip()
                        constraints += f" FOREIGN KEY ({column_name}) REFERENCES {reference_table}({reference_column})"
                
                # Add constraints to column definition
                column_definition = f"{column_name} {column_type} {constraints}".strip()
                columns.append(column_definition)

            # Join all columns into one string for the CREATE TABLE statement
            columns_sql = ",".join(columns)

            # Create the final CREATE TABLE SQL statement
            create_table_sql = f"CREATE TABLE {table_name} ({columns_sql})"

            # Show an example to the user
            print(f"\n{Colors.MAGENTA}Example of a valid table definition:{Colors.RESET}")
            print(f"{Colors.CYAN}CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, age INT){Colors.RESET}")
            print(f"\n{Colors.YELLOW}Your SQL statement will be:{Colors.RESET}")
            print(f"{Colors.CYAN}{create_table_sql}{Colors.RESET}")

            # Execute the SQL command to create the table
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
            connection.commit()
            print(f"{Colors.GREEN}Table '{table_name}' created successfully!{Colors.RESET}")
            
            # Now, insert values into the table
            insert_values(connection, table_name, columns)
            
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number of columns.{Colors.RESET}")
        except Error as e:
            print(f"{Colors.RED}Error: {e}{Colors.RESET}")
    else:
        print(f"{Colors.RED}Please enter a valid table name.{Colors.RESET}")

def insert_values(connection, table_name, columns):
    # Generate the column names and placeholders for the SQL INSERT statement
    column_names = ", ".join([col.split()[0] for col in columns])
    placeholders = ", ".join(["%s" for _ in columns])

    # Prepare the INSERT SQL statement
    insert_sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"

    try:
        cursor = connection.cursor()
        
        # Ask the user to enter values for each column
        values = []
        for col in columns:
            column_name = col.split()[0]  # Extract column name from column definition
            value = input(f"{Colors.YELLOW}Enter value for '{column_name}': {Colors.RESET}").strip()
            
            # Check the data type of the column
            column_type = col.split()[1].upper()

            if column_type == 'INT':
                # Convert the value to an integer if the column type is INT
                if value.isdigit():
                    values.append(int(value))
                else:
                    print(f"{Colors.RED}Please enter a valid integer value for '{column_name}'.{Colors.RESET}")
                    return
            elif column_type == 'VARCHAR':
                # For VARCHAR, just append the string value
                values.append(value)
            else:
                # Handle other data types if needed
                values.append(value)

        # Insert the values into the table
        cursor.execute(insert_sql, values)
        connection.commit()  # Commit the transaction
        print(f"{Colors.GREEN}Values inserted successfully into '{table_name}'!{Colors.RESET}")
    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def main_menu():
    connection = create_connection()
    if not connection:
        return
    while True:
        print(f"\n{Colors.MAGENTA}Main Menu:{Colors.RESET}")
        print(f"{Colors.BLUE}1. Show Databases     2. Create Database     3. Drop Database{Colors.RESET}")
        print(f"{Colors.BLUE}4. Use Database       5. Table Operations     6. Exit{Colors.RESET}")

        choice = input(f"{Colors.YELLOW}Enter your choice (1/2/3/4/5/6): {Colors.RESET}").strip()

        if choice == '1':
            show_databases(connection)
        elif choice == '2':
            create_database(connection)
        elif choice == '3':
            drop_database(connection)
        elif choice == '4':
            use_database(connection)
        elif choice == '5':
            table_operations(connection)
        elif choice == '6':
            print(f"{Colors.RED}Exiting program.{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}Invalid choice, Try again!{Colors.RESET}")


def describe_table(connection):
    try:
        # Show tables in the current database
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        if not tables:
            print(f"{Colors.RED}No tables available in the current database.{Colors.RESET}")
            return

        print(f"{Colors.YELLOW}Available Tables:{Colors.RESET}")
        for i, table in enumerate(tables, 1):
            print(f"{Colors.CYAN}{i}. {table[0]}{Colors.RESET}")

        # Ask the user to select a table to describe
        table_choice = input(f"{Colors.YELLOW}Select a table to describe (1-{len(tables)}): {Colors.RESET}").strip()
        if not table_choice.isdigit() or int(table_choice) < 1 or int(table_choice) > len(tables):
            print(f"{Colors.RED}Invalid choice.{Colors.RESET}")
            return

        selected_table = tables[int(table_choice) - 1][0]
        print(f"{Colors.GREEN}You selected table: {selected_table}{Colors.RESET}")

        # Fetch the description of the selected table
        cursor.execute(f"DESCRIBE {selected_table}")
        columns = cursor.fetchall()

        if not columns:
            print(f"{Colors.RED}No columns found for the selected table.{Colors.RESET}")
            return

        print(f"\n{Colors.YELLOW}Description of '{selected_table}':{Colors.RESET}")
        for column in columns:
            print(f"{Colors.CYAN}{column[0]}{Colors.RESET} | Type: {column[1]} | Null: {column[2]} | Key: {column[3]} | Default: {column[4]} | Extra: {column[5]}")

    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def drop_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        if not tables:
            print(f"{Colors.RED}No tables available to drop.{Colors.RESET}")
            return
        
        print(f"{Colors.YELLOW}Available Tables to Drop:{Colors.RESET}")
        for i, table in enumerate(tables, 1):
            print(f"{Colors.CYAN}{i}. {table[0]}{Colors.RESET}")

        table_choice = input(f"{Colors.YELLOW}Select a table to drop (1-{len(tables)}): {Colors.RESET}").strip()
        if not table_choice.isdigit() or int(table_choice) < 1 or int(table_choice) > len(tables):
            print(f"{Colors.RED}Invalid choice.{Colors.RESET}")
            return
        
        selected_table = tables[int(table_choice) - 1][0]
        print(f"{Colors.GREEN}You selected table: {selected_table}{Colors.RESET}")

        confirm = input(f"{Colors.RED}Are you sure you want to drop the table '{selected_table}'? (y/n): {Colors.RESET}").strip().lower()
        if confirm == 'y':
            cursor.execute(f"DROP TABLE {selected_table}")
            connection.commit()
            print(f"{Colors.GREEN}Table '{selected_table}' has been dropped successfully.{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}Operation cancelled.{Colors.RESET}")

    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")
            
def table_operations(connection):
    while True:
        print(f"\n{Colors.MAGENTA}Table Operations:{Colors.RESET}")
        print(f"{Colors.BLUE}1. Show Tables      2. Create New Table      3. Insert Values{Colors.RESET}")
        print(f"{Colors.BLUE}4. View Data        5. Drop Table            6. Join Tables{Colors.RESET}")
        print(f"{Colors.BLUE}7. Delete Row       8. Go Back{Colors.RESET}")

        choice = input(f"{Colors.YELLOW}Enter your choice (1/2/3/4/5/6/7/8): {Colors.RESET}").strip()

        if choice == '1':
            show_table(connection)
        elif choice == '2':
            create_table(connection)
        elif choice == '3':
            insert_into_existing_table(connection)
        elif choice == '4':
            view_table_data(connection)
        elif choice == '5':
            drop_table(connection)
        elif choice == '6':
            join_tables(connection)
        elif choice == '7':
            delete_row(connection)  # Added delete row option
        elif choice == '8':
            break  # Go back to the main menu
        else:
            print(f"{Colors.RED}Invalid choice, please try again.{Colors.RESET}")

# New Function: Delete Row
def delete_row(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        if not tables:
            print(f"{Colors.RED}No tables available in the current database.{Colors.RESET}")
            return
        
        print(f"{Colors.YELLOW}Available Tables:{Colors.RESET}")
        for i, table in enumerate(tables, 1):
            print(f"{Colors.CYAN}{i}. {table[0]}{Colors.RESET}")

        table_choice = input(f"{Colors.YELLOW}Select a table from which to delete a row (1-{len(tables)}): {Colors.RESET}").strip()
        if not table_choice.isdigit() or int(table_choice) < 1 or int(table_choice) > len(tables):
            print(f"{Colors.RED}Invalid choice.{Colors.RESET}")
            return
        
        selected_table = tables[int(table_choice) - 1][0]
        print(f"{Colors.GREEN}You selected table: {selected_table}{Colors.RESET}")

        # Show the columns of the selected table to help identify the primary key or unique column
        cursor.execute(f"DESCRIBE {selected_table}")
        columns = cursor.fetchall()

        print(f"\n{Colors.YELLOW}Columns in '{selected_table}':{Colors.RESET}")
        for column in columns:
            print(f"{Colors.CYAN}{column[0]}{Colors.RESET}")

        column_choice = input(f"{Colors.YELLOW}Select the column to filter the row for deletion (by unique ID or primary key): {Colors.RESET}").strip()
        row_value = input(f"{Colors.YELLOW}Enter the value of '{column_choice}' for the row to delete: {Colors.RESET}").strip()

        # Prepare and execute the DELETE query
        delete_sql = f"DELETE FROM {selected_table} WHERE {column_choice} = %s"
        cursor.execute(delete_sql, (row_value,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"{Colors.GREEN}Row deleted successfully from '{selected_table}'{Colors.RESET}")
        else:
            print(f"{Colors.RED}No rows found with the value '{row_value}' in column '{column_choice}'{Colors.RESET}")
    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def join_tables(connection):
    try:
        # Show tables in the current database
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        if not tables:
            print(f"{Colors.RED}No tables available in the current database.{Colors.RESET}")
            return

        print(f"{Colors.YELLOW}Available Tables:{Colors.RESET}")
        for i, table in enumerate(tables, 1):
            print(f"{Colors.CYAN}{i}. {table[0]}{Colors.RESET}")

        # Ask the user to select two tables for the join
        table_choice_1 = input(f"{Colors.YELLOW}Select the first table for the join (1-{len(tables)}): {Colors.RESET}").strip()
        table_choice_2 = input(f"{Colors.YELLOW}Select the second table for the join (1-{len(tables)}): {Colors.RESET}").strip()

        if not table_choice_1.isdigit() or not table_choice_2.isdigit() or int(table_choice_1) < 1 or int(table_choice_1) > len(tables) or int(table_choice_2) < 1 or int(table_choice_2) > len(tables):
            print(f"{Colors.RED}Invalid choice.{Colors.RESET}")
            return
        
        table_1 = tables[int(table_choice_1) - 1][0]
        table_2 = tables[int(table_choice_2) - 1][0]

        print(f"{Colors.GREEN}You selected tables: {table_1} and {table_2}{Colors.RESET}")

        # Ask the user to select the type of join
        print(f"\n{Colors.YELLOW}Select the type of join:{Colors.RESET}")
        print(f"{Colors.CYAN}1. INNER JOIN{Colors.RESET}")
        print(f"{Colors.CYAN}2. LEFT JOIN{Colors.RESET}")
        print(f"{Colors.CYAN}3. RIGHT JOIN{Colors.RESET}")
        print(f"{Colors.CYAN}4. FULL OUTER JOIN{Colors.RESET}")

        join_type_choice = input(f"{Colors.YELLOW}Enter your choice (1/2/3/4): {Colors.RESET}").strip()

        if join_type_choice not in ['1', '2', '3', '4']:
            print(f"{Colors.RED}Invalid choice.{Colors.RESET}")
            return

        join_type_mapping = {
            '1': 'INNER JOIN',
            '2': 'LEFT JOIN',
            '3': 'RIGHT JOIN',
            '4': 'FULL OUTER JOIN'
        }

        join_type = join_type_mapping[join_type_choice]

        # Ask the user to specify the columns to join on
        column_1 = input(f"{Colors.YELLOW}Enter the column from '{table_1}' to join on: {Colors.RESET}").strip()
        column_2 = input(f"{Colors.YELLOW}Enter the column from '{table_2}' to join on: {Colors.RESET}").strip()

        # Construct the SQL JOIN query
        if join_type == 'FULL OUTER JOIN':
            # For FULL OUTER JOIN, MySQL does not directly support FULL OUTER JOIN. We can use a UNION of LEFT JOIN and RIGHT JOIN
            join_sql = f"""
                SELECT * FROM {table_1} LEFT JOIN {table_2} ON {table_1}.{column_1} = {table_2}.{column_2}
                UNION
                SELECT * FROM {table_1} RIGHT JOIN {table_2} ON {table_1}.{column_1} = {table_2}.{column_2}
            """
        else:
            # For INNER, LEFT, and RIGHT JOIN, we can use standard join syntax
            join_sql = f"""
                SELECT * FROM {table_1} {join_type} {table_2} ON {table_1}.{column_1} = {table_2}.{column_2}
            """
        
        cursor.execute(join_sql)
        rows = cursor.fetchall()

        if rows:
            print(f"\n{Colors.GREEN}Join Results:{Colors.RESET}")
            for row in rows:
                print(row)
        else:
            print(f"{Colors.RED}No results found for the join operation.{Colors.RESET}")

    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")
            
def view_table_data(connection):
    try:
        # Show tables in the current database
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        if not tables:
            print(f"{Colors.RED}No tables available in the current database.{Colors.RESET}")
            return

        print(f"{Colors.YELLOW}Available Tables:{Colors.RESET}")
        for i, table in enumerate(tables, 1):
            print(f"{Colors.CYAN}{i}. {table[0]}{Colors.RESET}")

        # Ask the user to select a table
        table_choice = input(f"{Colors.YELLOW}Select a table to view data (1-{len(tables)}): {Colors.RESET}").strip()
        if not table_choice.isdigit() or int(table_choice) < 1 or int(table_choice) > len(tables):
            print(f"{Colors.RED}Invalid choice.{Colors.RESET}")
            return
        
        selected_table = tables[int(table_choice) - 1][0]
        print(f"{Colors.GREEN}You selected table: {selected_table}{Colors.RESET}")

        # Fetch data from the selected table
        cursor.execute(f"SELECT * FROM {selected_table}")
        rows = cursor.fetchall()

        if not rows:
            print(f"{Colors.RED}No data found in the table '{selected_table}'.{Colors.RESET}")
            return

        print(f"\n{Colors.YELLOW}Data in '{selected_table}':{Colors.RESET}")
        for row in rows:
            print(f"{Colors.CYAN}{row}{Colors.RESET}")
    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def insert_into_existing_table(connection):
    try:
        # Show tables in the current database
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        if not tables:
            print(f"{Colors.RED}No tables available in the current database.{Colors.RESET}")
            return

        print(f"{Colors.YELLOW}Available Tables:{Colors.RESET}")
        for i, table in enumerate(tables, 1):
            print(f"{Colors.CYAN}{i}. {table[0]}{Colors.RESET}")

        # Ask the user to select a table
        table_choice = input(f"{Colors.YELLOW}Select a table to insert values into (1-{len(tables)}): {Colors.RESET}").strip()
        if not table_choice.isdigit() or int(table_choice) < 1 or int(table_choice) > len(tables):
            print(f"{Colors.RED}Invalid choice.{Colors.RESET}")
            return
        
        selected_table = tables[int(table_choice) - 1][0]
        print(f"{Colors.GREEN}You selected table: {selected_table}{Colors.RESET}")

        # Fetch columns from the selected table to show to the user
        cursor.execute(f"DESCRIBE {selected_table}")
        columns = cursor.fetchall()

        if not columns:
            print(f"{Colors.RED}No columns found for the selected table.{Colors.RESET}")
            return

        print(f"\n{Colors.YELLOW}Columns in '{selected_table}':{Colors.RESET}")
        column_definitions = []
        for column in columns:
            print(f"{Colors.CYAN}{column[0]}{Colors.RESET} ({column[1]})")
            column_definitions.append(f"{column[0]} {column[1]}")

        # Now, insert values into the selected table
        insert_values(connection, selected_table, column_definitions)

    except Error as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

if __name__ == "__main__":
    main_menu()

