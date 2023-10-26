import pyodbc
import pandas as pd
import vanna as vn
import time




def run_vanna_sql_sqlServer(server: str, database: str,sql: str) -> pd.DataFrame:
    conn
    try:
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION=yes'
        conn = pyodbc.connect(connection_string)
        if sql is None:
            conn.close()
            return
        else:
            df = pd.read_sql(str(sql), conn)
            conn.close()
            return df
    except Exception as e:
        #If connection to db is still open --> Close
        if conn: 
         conn.close()
        print(f"Error in connection: {str(e)}")

def get_clear_string(string: str) -> str:
     tmp = str(string)
     tmp = tmp.replace('\\n',' ')
     tmp = tmp.replace('\\r',' ')
     tmp = tmp.replace('\\t',' ')
     tmp = tmp[2:]
     tmp = tmp[:-3]
     return tmp



   
   
   