from flask import Flask, render_template,jsonify,request
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS,cross_origin
import database as db
import os

# Create the application to serve.
app = Flask(__name__)
socketio = SocketIO(app)

# We want our app to communicate with Vuejs, so we need to enable cross origin requests to get stuff from other ports
CORS(app,resources={r'/*': {'origins':'*'}})

#TODO This function will find out which HTTP method we are using and parse the incoming json. 
# it supports only 2 HTTP types, GET and POST. If it's POST, we take the json and then 
# add it to the Database based on the header (another feature I will implement in the Home.vue component)
# and then we send that JSON back to the Vue front end with another
# post request where we add it to our table to display.
# If it is a GET request then we will parse the json again and see what it's requesting, then return the 
# entry from the database in a post towards the frontend. 
# 
# NOTE a GET request will appear whenever we visit port 5000, so don't visit that port
# or it may break the code. We could fix this, but it'd be kinda boring 
# and useless since this page isn't normally visited when using our app.

@app.route('/', methods=['GET','POST','DELETE','MODIFY']) # we'll need to define this route as '*' later on for more views.
def handle_requests():
    db.db_init()
    if request.method == 'POST':
        print(request.json)
        
        if  request.json['header'] == 'insert':
            db.db_insert(request.json)

        if request.json['header']  == 'update':
            db.db_update(request.json)

        return str(request.method)

    if request.method == 'GET':

        if request.json['header']  == 'search':
            db.db_search

        return str(request.method)

# This actually runs the server, it's on port 5000, which is a separate port from the vue frontend, since we can't run
# two servers on one port.
if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000)

    
