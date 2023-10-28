from flask import Flask,request
import json
import databaseUtilities
import clsResponse
import vannaUtilities

# Create a Flask web server
app = Flask(__name__)

# Define a route for the root URL ("/") that returns "Hello, World!"
@app.route('/generateSQL', methods=['POST'])
def generate_sql():
     try:   
      return None
     except Exception as e:
         print("An error occurred:", e)
         return 
#Request Json {"server": "LAPTOP-M522HAH2\\SQLEXPRESS","db":"STAN_STEFAN"}     
@app.route('/getDatabaseTableNames', methods=['POST'])
def get_database_tables():
     try:   
      requestDataDict = request.get_json()
      serverValue = requestDataDict['server']
      dbValue = requestDataDict['db']
      respdata = databaseUtilities.retrieve_names_of_all_tables(serverValue,dbValue)
      #class to dictionary
      obj_dict = vars(respdata)
      return obj_dict
     except Exception as e:
         response = clsResponse.Response(False,str(e),None)
         return response 

#Request Json {"server": "LAPTOP-M522HAH2\\SQLEXPRESS","db":"STAN_STEFAN"} 
@app.route('/getDatabaseViewsNames', methods=['POST'])
def get_database_views():
     try:   
      requestDataDict = request.get_json()
      serverValue = requestDataDict['server']
      dbValue = requestDataDict['db']
      respdata = databaseUtilities.retrieve_names_of_all_views(serverValue,dbValue)
      #class to dictionary
      obj_dict = vars(respdata)
      return obj_dict
     except Exception as e:
         response = clsResponse.Response(False,str(e),None)
         return response 
#Request Json {"model": "aModelJustForTest"}
@app.route('/createModel', methods=['POST'])
def createModel():
   try:   
      requestDataDict = request.get_json()
      modelName = requestDataDict['model']
      respdata = vannaUtilities.create_new_model(modelName)
      obj_dict = vars(respdata)
      return obj_dict
   except Exception as e:
         response = clsResponse.Response(False,str(e),None)
         return response 
"""
{"model": "m_ssfan",
  "server": "LAPTOP-M522HAH2\\SQLEXPRESS",
  "db":"STAN_STEFAN",
  "desired_table_names":["MTRL", "MTRGROUP", "MTRMARK", "MTRMODEL"]
 }
"""
@app.route('/trainWithTables', methods=['POST'])
def trainWithTables():
   try:   
      requestDataDict = request.get_json()
      modelName = requestDataDict['model']
      server = requestDataDict['server']
      db = requestDataDict['db']
      desired_table_names = requestDataDict['desired_table_names']
      respdata = vannaUtilities.train_with_tables(modelName,server,db,desired_table_names)
      obj_dict = vars(respdata)
      return obj_dict
   except Exception as e:
         response = clsResponse.Response(False,str(e),None)
         return response 
   
"""
{"model": "m_ssfan",
  "server": "LAPTOP-M522HAH2\\SQLEXPRESS",
  "db":"STAN_STEFAN",
  "desired_table_names":["cccVMtrlDim"]
 }
"""
@app.route('/trainWithViews', methods=['POST'])
def trainWithViews():
   try:   
      requestDataDict = request.get_json()
      modelName = requestDataDict['model']
      server = requestDataDict['server']
      db = requestDataDict['db']
      desired_view_names = requestDataDict['desired_view_names']
      respdata = vannaUtilities.train_with_views(modelName,server,db,desired_view_names)
      obj_dict = vars(respdata)
      return obj_dict
   except Exception as e:
         response = clsResponse.Response(False,str(e),None)
         return response 
"""
{"model": "m_ssfan",
 "statement":"The MTRL contains the products infos"
 }
"""
@app.route('/trainWithDDL', methods=['POST'])
def trainWithDDL():
   try:   
      requestDataDict = request.get_json()
      modelName = requestDataDict['model']
      statement = requestDataDict['statement']
      respdata = vannaUtilities.train_with_statement(modelName,statement,'ddl')
      obj_dict = vars(respdata)
      return obj_dict
   except Exception as e:
         response = clsResponse.Response(False,str(e),None)
         return response 

"""
{"model": "m_ssfan",
 "statement":"The MTRL contains the products infos"
 }
"""   
@app.route('/trainWithSQL', methods=['POST'])
def trainWithSQL():
   try:   
      requestDataDict = request.get_json()
      modelName = requestDataDict['model']
      statement = requestDataDict['statement']
      respdata = vannaUtilities.train_with_statement(modelName,statement,'sql')
      obj_dict = vars(respdata)
      return obj_dict
   except Exception as e:
         response = clsResponse.Response(False,str(e),None)
         return response 
"""
{"model": "m_ssfan",
 "statement":"The MTRL contains the products infos"
 }
"""   
@app.route('/trainWithDocumentation', methods=['POST'])
def trainWithDocumentation():
   try:   
      requestDataDict = request.get_json()
      modelName = requestDataDict['model']
      statement = requestDataDict['statement']
      respdata = vannaUtilities.train_with_statement(modelName,statement,'documentation')
      obj_dict = vars(respdata)
      return obj_dict
   except Exception as e:
         response = clsResponse.Response(False,str(e),None)
         return response 

# Run the Flask app on localhost, port 5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
