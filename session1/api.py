from flask import Flask,request
from flask_jwt_extended import 
from database import database_connect
import json
import requests

app=Flask(__name__)
app.

@app.route("/api/v1/SignIn",methods=["POST"])
def info():
    response=request.json()
    data=response.json()
    name=data["name"]
    pwd=data["password"]
    
    return name,pwd



# POST /api/v1/SignIn
# GET /api/v1/Documents
# GET /api/v1/Document/{documentId}/Comments


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)