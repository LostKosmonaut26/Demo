from flask import jsonify
import pyodbc
import json


class database_connect():
    def get_info(query):
        try:
            connect_str=pyodbc.connect("driver={ODBC Driver 17 for sql server};server=tcp:84.54.228.191,49172;database=Pushkarcki;UID=Pushkarcki;PWD=3kVJPI3h")
            cursor=connect_str.cursor()
            cursor.execute(query)
    
            rows=cursor.fetchall()
            columns=[column[0] for column in cursor.description]
            data=[dict(zip(columns,row))for row in rows]
                
            return jsonify(data)
            
        except pyodbc.Error as e:
            return f"Error: {e}" 
               
    def action_info(query):
        try:
            connect_str=pyodbc.connect()    
            cursor=connect_str.cursor()
            cursor.execute(query)

            cursor.commit()
            return "good"
        except pyodbc.Error as e:
            return f"Error: {e}" 