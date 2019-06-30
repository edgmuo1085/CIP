#!/usr/bin/env python
 
# Desarrollado por: Edgar Munoz
# Mi primer ventana
 
from flask import Flask
app = Flask(__name__)
  
@app.route("/")
def index():
    return "Index!"
  
@app.route("/hola")
def hello():
    return "Hola Mundo!"
  
@app.route("/miembros")
def members():
    return "Miembros"
  
@app.route("/members/<string:name>/")
def getMember(name):
    return name

#</string:name></string:name>
  
if __name__ == "__main__":
    app.run()

