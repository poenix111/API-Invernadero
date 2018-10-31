from flask import Flask, request,make_response
import mysql.connector
from usuario import Usuario

conexion = mysql.connector.connect(user="brian",password="12345",database="invernadero")
cursor = conexion.cursor()



app = Flask(__name__)


@app.route("/home/")
def hello():
    respuesta = make_response("Hello World")
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta



@app.route("/login/",methods = ['GET'])
def login():
    user = request.args.get('usuario')
    password = request.args.get('password')
    userDB = Usuario(conexion,cursor)
    print(user, password)
    print(userDB.login(user,password))
    return user + " " + password


app.run(debug=True)