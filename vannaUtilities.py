import pyodbc
import pandas as pd
import vanna as vn
import time
import clsResponse
import databaseUtilities


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

def create_new_model(modelName:str) -> clsResponse.Response:
    try:
        vn.set_api_key('d72ab2501d4e426e99baf6b5ed3e750e')
        success = vn.create_model(model= modelName, db_type="sqlServer")
        if(success):
            response = clsResponse.Response(True,'',None)
        else:
            response = clsResponse.Response(False,
                                            'The model does not created. Try Again with other name',
                                            None)
        return response
    except Exception as e:
        response = clsResponse.Response(False,e,None)
        return response
def train_with_tables(modelName:str,server: str,database: str,desired_table_names: list) -> clsResponse.Response:
    try:
        vn.set_api_key('d72ab2501d4e426e99baf6b5ed3e750e')
        vn.set_model(modelName)
        vn.run_sql = run_vanna_sql_sqlServer

        sqlTodb = ""
        #Get query from file
        with open('create_table_sql_generator.txt', 'r') as file:
            sqlTodb = file.read()
        for table_name in desired_table_names:
            sql_with_table = sqlTodb.replace('dbo.Table','dbo.'+str(table_name))
            sqlForDDL = databaseUtilities.simple_execute_sql_query(server,database,sql_with_table)
            if(None in sqlForDDL[0]):
              continue
            create_table_sql = get_clear_string(sqlForDDL[0])
            time.sleep(3)
            vn.train(ddl=str(create_table_sql))
        response = clsResponse.Response(True,'',None)
        return response
    except Exception as e:
        response = clsResponse.Response(False,e,None)
        return response

def train_with_views(modelName:str,server: str,database: str,desired_view_names: list) -> clsResponse.Response:
    try:
        vn.set_api_key('d72ab2501d4e426e99baf6b5ed3e750e')
        vn.set_model(modelName)
        vn.run_sql = run_vanna_sql_sqlServer

        for view in desired_view_names:
            sql = "SELECT OBJECT_DEFINITION(OBJECT_ID('"+view+"')) AS CreateViewCode"
            sqlForDDL = databaseUtilities.simple_execute_sql_query(server,database,sql)
            if(None in sqlForDDL[0]):
              continue
            create_view_sql = get_clear_string(sqlForDDL[0])
            time.sleep(3)
            vn.train(ddl=str(create_view_sql))
        response = clsResponse.Response(True,'',None)
        return response
    except Exception as e:
        response = clsResponse.Response(False,e,None)
        return response    

   
   
   