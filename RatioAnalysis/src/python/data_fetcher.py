#code to get data from API's
import yfinance as yf #yf is the alias - its to improve readability
import sqlite3 #sqlite3 is a module that allows you to work with the SQLite database
from datetime import datetime #datetime is a module that supplies classes for manipulating dates and times in both simple and complex ways

def fetch_n_store_data(ticker_symbol, db_path='data/financial_data.db'): #connect to SQLite -- open-source relational datanbase software
    conn = sqlite3.connect(db_path) #connect to the database; db_path is the path to the database file
    cursor = conn.cursor() #create a cursor object using the cursor() method

    #create tables in case they dont exist yet 
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS financial_data ( 
                   ticker TEXT,
                   date TEXT,
                   revenue REAL,
                   total_assets REAL,
                   total_liabilities REAL,
                   PRIMARY KEY (ticker, date)
    )    
    ''')

    #fetch and store data for each ticker (fetch = bringen)
    for ticker in ticker_symbol: 
        stock = yf.Ticker(ticker) #fetch data from Yahoo Finance API
        financials = stock.financials #fetch income st data
        balance_sheet = stock.balance_sheet #fetch balance sheet data

        #process and insert data 
        for date in financials.columns: #iterate over the columns of the financials dataframe
            try: 
                cursor.execute('''
                INSERT OR REPLACE INTO financial_data
                VALUES (?, ?, ?, ?, ?, ?)
                ''',(
                    ticker, date.strftime('%Y-%m-%d'),
                    financials.loc['Total Revenue', date] if 'Total Revenue' in financials.index else None,
                    financials.loc['Net Income', date] if 'Net Income' in financials.index else None,
                    financials.loc['Credit Sales', date] if 'Credit Sales' in financials.index else None,
                    financials.loc['Gross Profit', date] if 'Gross Profit' in financials.index else None,
                    balance_sheet.loc['Inventory', date]if 'Inventory' in balance_sheet.index else None,
                    balance_sheet.loc['Accounts Receivables', date]if 'Accounts Receivables' in balance_sheet.index else None,
                    balance_sheet.loc['Equity', date]if 'Equity' in balance_sheet.index else None,
                    balance_sheet.loc['Current Liabilities', date]if 'Current Liabilities' in balance_sheet.index else None,
                    balance_sheet.loc['Fixed Assets', date]if 'Fixed Assets' in balance_sheet.index else None,
                    balance_sheet.loc['Current Assets', date]if 'Current Assets' in balance_sheet.index else None,
                    balance_sheet.loc['Total Assets', date] if 'Total Assets' in balance_sheet.index else None,
                    balance_sheet.loc['Total Liabilities', date] if 'Total Liabilities' in balance_sheet.index else None
                ))  
            except Exception as e: #catch any exceptions that occur during the process
                print(f"Error processesing {ticker} for {date}: {e}")
    conn.commit() #commit the changes to the database
    conn.close() #close the connection to the database
if __name__ == "__main__":
    tickers = ['AAPLE', 'MSFT', 'GOOGL']
    fetch_n_store_data(tickers)
            
