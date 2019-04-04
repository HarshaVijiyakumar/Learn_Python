import sqlite3

class DatabaseConnection: # created this class for context manager
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect('data.db')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is not None or exc_type is not None or exc_val is not None:
            self.connection.commit()
        else:
            self.connection.commit()
            self.connection.close()

