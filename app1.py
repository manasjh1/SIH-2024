import mysql.connector
import csv
import os
import re

def connect_mysql(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def sanitize_table_name(name):
    # Replace spaces and other problematic characters with underscores
    sanitized = re.sub(r'[^\w]', '_', name)
    # Ensure the name doesn't start with a number
    if sanitized[0].isdigit():
        sanitized = f"t_{sanitized}"
    return sanitized

def sanitize_column_name(name):
    # Replace problematic characters with underscores
    sanitized = re.sub(r'[^\w\s()]', '_', name)
    # Ensure the name doesn't start with a number
    if sanitized[0].isdigit():
        sanitized = f"col_{sanitized}"
    return sanitized

def import_csv_to_mysql(connection, csv_file, table_name):
    cursor = connection.cursor()
    
    try:
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            csv_reader = csv.reader(f)
            headers = next(csv_reader)
        
        safe_table_name = sanitize_table_name(table_name)
        
        # Create a mapping of original to sanitized column names
        column_mapping = {header: sanitize_column_name(header) for header in headers}
        
        create_table_query = f"CREATE TABLE IF NOT EXISTS `{safe_table_name}` (id INT AUTO_INCREMENT PRIMARY KEY"
        for original, sanitized in column_mapping.items():
            create_table_query += f", `{sanitized}` VARCHAR(255) COMMENT '{original}'"
        create_table_query += ")"
        
        print(f"Executing query: {create_table_query}")
        cursor.execute(create_table_query)
        
        placeholders = ', '.join(['%s'] * len(headers))
        insert_query = f"INSERT INTO `{safe_table_name}` ({', '.join([f'`{column_mapping[h]}`' for h in headers])}) VALUES ({placeholders})"
        
        row_count = 0
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # skip header row
            for row in csv_reader:
                if len(row) != len(headers):
                    print(f"Warning: Row {row} has {len(row)} columns, expected {len(headers)}")
                    continue
                cursor.execute(insert_query, row)
                row_count += 1
        
        connection.commit()
        print(f"Inserted {row_count} rows into table {safe_table_name}")
        
        # Verify table structure
        cursor.execute(f"SHOW FULL COLUMNS FROM `{safe_table_name}`")
        table_structure = cursor.fetchall()
        print(f"\nTable structure for {safe_table_name}:")
        for column in table_structure:
            print(f"Column: {column[0]}, Type: {column[1]}, Original Name: {column[8]}")
        
        print(f"\nTo query this table, use: SELECT * FROM `{safe_table_name}`;")
        
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def import_multiple_csv_files(connection, csv_directory, table_prefix=''):
    for filename in os.listdir(csv_directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(csv_directory, filename)
            table_name = f"{table_prefix}{os.path.splitext(filename)[0]}"
            print(f"\nImporting {filename} into table {table_name}...")
            import_csv_to_mysql(connection, file_path, table_name)
            print(f"Finished importing {filename}")

# main execution
if __name__ == "__main__":
    try:
        connection = connect_mysql("localhost", "root", "12345678", "judes")
        
        csv_directory = r"C:\Users\SHI\Desktop\om.html\__MACOSX\Dicee Challenge - Starting Files\api-ml\csv_directory"
        
        table_prefix = "listHCjudges_"
        import_multiple_csv_files(connection, csv_directory, table_prefix)
        
    except mysql.connector.Error as err:
        print(f"MySQL Connection Error: {err}")
    except Exception as e:
        print(f"General Error: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

    print("Script execution completed.")