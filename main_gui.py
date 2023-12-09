# import all necessary libraries
import tkinter as tk
from tkinter import filedialog
import psycopg2
from psycopg2 import sql

# PostgreSQL connection parameters
db_params = {
    'host': 'localhost',
    'database': 'test_db', # database name
    'user': 'postgres', # your postgres username
    'password': 'aldrin_02',  # your postgres password
}


# Your postgres table name
table_name = "sales"

# Define the main application class
class CSVImporterApp:
    def __init__(self, root):
        # Initialize the application with a Tkinter root window
        self.root = root
        self.root.title("CSV to PostgreSQL Importer")

        # Create and pack widgets
        self.label = tk.Label(root, text="Select CSV File:")
        self.label.pack(pady=10)

        # Create first button UI
        self.browse_button = tk.Button(
            root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        # Create second button UI
        self.import_button = tk.Button(
            root, text="Import to PostgreSQL", command=self.import_to_postgresql)
        self.import_button.pack(pady=10)

    # function to browse file
    def browse_file(self):
        # Open a file dialog to select a CSV file
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        self.label.config(text=f"Selected File: {file_path}")
        self.csv_file_path = file_path

    # function to import file to postgresql
    def import_to_postgresql(self):
        try:
            # Establish a connection to PostgreSQL
            conn = psycopg2.connect(**db_params)
            cursor = conn.cursor()

            # Use the COPY command to import data from CSV
            copy_query = f"COPY order_schema.\"{table_name}\" FROM STDIN WITH CSV HEADER DELIMITER ','"

            # Open the CSV file and execute the copy_expert method
            with open(self.csv_file_path, 'r') as csv_file:
                cursor.copy_expert(sql.SQL(copy_query), csv_file)

            # Commit the changes and close the connection
            conn.commit()
            cursor.close()
            conn.close()

            print("Import successful!")

        except Exception as e:
            # Print an error message if an exception occurs
            print(f"Error: {e}")


# Main program entry point
if __name__ == "__main__":
    # Create a Tkinter root window and initialize the application
    root = tk.Tk()
    app = CSVImporterApp(root)
    root.mainloop()
