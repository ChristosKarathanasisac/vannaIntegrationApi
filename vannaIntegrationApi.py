from flask import Flask,request
import json
import databaseUtilities
import clsResponse

# Create a Flask web server
app = Flask(__name__)

# Define a route for the root URL ("/") that returns "Hello, World!"
@app.route('/generateSQL', methods=['POST'])
def generate_sql():
     try:   
      responsedata = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
      return responsedata
     except Exception as e:
         print("An error occurred:", e)
         return 
     
@app.route('/getDatabaseTablenames', methods=['POST'])
def get_database_tables():
     try:   
      print('in getDatabaseTablenames')
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

# Run the Flask app on localhost, port 5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
