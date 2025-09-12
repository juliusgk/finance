import sqlite3
import pandas as pd

class Financial_DB_Manager:
    def __init__(self, db_path='/data/financail_data.db'):
        self.db_path = db_path 

    def initialize_db(self):
        """Create the database schema if it doesn't exist"""
        conn = sqlite3.connect(self.db_path) #used to as a common abbreviation for connection //stores connection between external resource (eg db)
        cursor = conn.cursor() #cursor - middleware between SQLite DB and SQL query // make connection for executing SQL queries 

        #create main financial data table 
        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS financial_data (
                       ticker TEXT,
                       date TEXT,
                       revenue REAL,
                       net_income REAL,
                       total_assets REAL,
                        total_liabilities REAL,
                        cash_flow REAL,
                        shares_outstanding REAL,
                        PRIMARY KEY (ticker, date)
        )
        ''')

        #create a table for storing metadata about updates
        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS metadata (
                       last_update TEXT,
                       source TEXT,
                       tickers_updated TEXT
        )
        ''')

        conn.commit() #sends a statement to the mysql server - commiting the current transaction
        conn.close() #closes the connection to the database

        def store_financial_data(self, data_df):
            """Store pandas DataFrame of financial data to SQLite"""
            conn = sqlite3.connect(self.db_path) #connect to database
            data_df.to_sql('financial_data', conn, if_exists='append', index=False)
            conn.close()
        
        def get_financial_data(self, ticker = None, start_date = None, end_date=None):
            """Retrieve financial data as pandas DataFrane with optional filters"""
            conn = sqlite3.connect(self.db_path)

            query = "SELECT * FROM financial_data"
            conditions = [] #normales array
            params = [] #normales array

            if ticker: 
                conditions.append("ticker = ?")
                params.append(ticker)
            
            if start_date:
                conditions.append("date >= ?")
                params.append(start_date)
            
            if end_date:
                conditions.append("date <= ?")
                params.append(end_date)
            
            if conditions:
                query += "WHERE" + "AND".join(conditions)
            
            df = pd.read_sql_query(query, conn, params=params)
            conn.close()
            return df
        def log_update(self, source, tickers_updated):
            """Log metadata about database updates"""
            import datetime
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute (
            "INSERT INTO metadata VALUES (?,?,?)",
                (datetime.datetime.now().isoform(), source, ','.join(tickers_updated))
            )

            conn.commit()
            conn.close()
            
