from flask import Flask, request, make_response, jsonify
from models.connection.connection import DbConnectionHandler
from models.repository.Connection_repository import ConnectionRepository

db_handle = DbConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()
connection_repository = ConnectionRepository(db_connection)

app = Flask(__name__)

@app.route('/api/users/', methods=['GET'])
def list_of_users():
    pass

@app.route('/api/users/insert/', methods=['POST'])
def create_user():
    new_user = request.json
    connection_repository.insert_document(new_user)
    return make_response(jsonify(message='new_user_infos', data=new_user))

app.run()
