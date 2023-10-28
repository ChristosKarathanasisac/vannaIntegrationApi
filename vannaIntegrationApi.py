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
@app.route('/trainModelWithDDL', methods=['POST'])
def trainModelWithDDL():
   try:   
      requestDataDict = request.get_json()
      serverValue = requestDataDict['model']
      #dbValue = requestDataDict['db']
      respdata = databaseUtilities.retrieve_names_of_all_views(serverValue,dbValue)
      #class to dictionary
      obj_dict = vars(respdata)
      return obj_dict
   except Exception as e:
         response = clsResponse.Response(False,str(e),None)
         return response 
   
@app.route('/trainModelWithDocumentation', methods=['POST'])
def trainModelWithDocumentation():
   
@app.route('/trainModelWithDocumentation', methods=['POST'])
def trainModelWithSQL():
"""

   
   

# Run the Flask app on localhost, port 5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
