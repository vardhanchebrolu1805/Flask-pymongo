from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# REST API endpoints for CRUD operations on User resource
@app.route('/users', methods=['GET'])
def get_all_users():
    users = db.users.find()
    output = []
    for user in users:
        output.append({
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })
    return jsonify(output)

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = db.users.find_one({'id': id})
    if user:
        output = {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        }
        return jsonify(output)
    else:
        return jsonify({'error': 'User not found'})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    id = data['id']
    name = data['name']
    email = data['email']
    password = data['password']
    db.users.insert_one({'id': id, 'name': name, 'email': email, 'password': password})
    return jsonify({'message': 'User created successfully'})

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    db.users.update_one({'id': id}, {'$set': {'name': name, 'email': email, 'password': password}})
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    db.users.delete_one({'id': id})
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
