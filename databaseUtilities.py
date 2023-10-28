import pyodbc
import pandas as pd
import clsResponse

def execute_sql_query(server: str, database: str,sql: str)->clsResponse.Response:
        conn = None
        try: 
         connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION=yes'
         conn = pyodbc.connect(connection_string)
         cursor = conn.cursor()
         cursor.execute(sql)
         rows = cursor.fetchall()

         if rows is not None:
            #resultDict = {key: None for key, in rows}
            rowsList = []
            for r in rows:
               rowsList.append(str(r[0]))

            response = clsResponse.Response(True,'',rowsList)
            return response
         else:
            response = clsResponse.Response(True,'Not found data',None)
            return response
        except Exception as e:
        #If connection to db is still open --> Close
         if conn: 
          conn.close()
         response = clsResponse.Response(False,str(e),None)
         return response

def retrieve_names_of_all_tables(server: str,database: str)->clsResponse.Response:
   try:
    sql = 'SELECT table_name FROM information_schema.tables'
    resp =  execute_sql_query(server,database,sql)
    if(resp.success):
       response = clsResponse.Response(True,'',resp.data)
    else:
       response = clsResponse.Response(True,resp.error,None)
    return response
   except Exception as e:
    response = clsResponse.Response(False,str(e),None)
    return response
   
def retrieve_names_of_all_views(server: str,database: str)->clsResponse.Response:
   try:
    sqlTodb = ""
    #Open the query from file
    sql = 'SELECT name FROM sys.views;'
    resp =  execute_sql_query(server,database,sql)
    if(resp.success):
       response = clsResponse.Response(True,'',resp.data)
    else:
       response = clsResponse.Response(True,resp.error,None)
    return response
   except Exception as e:
    response = clsResponse.Response(False,str(e),None)
    return response
   
def simple_execute_sql_query(server: str, database: str,sql: str):  
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION=yes'
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows