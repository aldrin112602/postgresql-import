import tkinter as tk
from tkinter import filedialog
import psycopg2
from psycopg2 import sql

# PostgreSQL connection parameters
db_params = {
    'host': 'localhost',
    'database': 'test_db',
    'user': 'postgres',
    'password': 'aldrin_02',
}

table_name = "sales"


class CSVImporterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV to PostgreSQL Importer")

        # Create and pack widgets
        self.label = tk.Label(root, text="Select CSV File:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(
            root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.import_button = tk.Button(
            root, text="Import to PostgreSQL", command=self.import_to_postgresql)
        self.import_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        self.label.config(text=f"Selected File: {file_path}")
        self.csv_file_path = file_path

    def import_to_postgresql(self):
        try:
            conn = psycopg2.connect(**db_params)
            cursor = conn.cursor()

            # Use the COPY command to import data from CSV
            copy_query = f"COPY order_schema.\"{table_name}\" FROM STDIN WITH CSV HEADER DELIMITER ','"

            with open(self.csv_file_path, 'r') as csv_file:
                cursor.copy_expert(sql.SQL(copy_query), csv_file)

            conn.commit()
            cursor.close()
            conn.close()

            print("Import successful!")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVImporterApp(root)
    root.mainloop()
