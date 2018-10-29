from flask import Flask, request
import mysql.connector
from usuario import Usuario

conexion = mysql.connector.connect(user="brian",password="12345",database="invernadero")
cursor = conexion.cursor()



app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"



@app.route("/login/",methods = ['GET'])
def login():
    user = request.args.get('usuario')
    password = request.args.get('password')
    userDB = Usuario(conexion,cursor)
    print(user, password)
    print(userDB.login(user,password))
    return user + " " + password


app.run(debug=True)