from flask import Flask, request, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/mlop_task_5_i202478'
mongo = PyMongo(app)


@app.route('/users', methods=['GET'])
def users():
    users = mongo.db.users.find()
    response = []
    for user in users:
        response.append({'name': user['name'], 'email': user['email']})
    return jsonify(response), 200


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json 
    name = data.get('name')
    email = data.get('email')

    if name and email:
        # Insert data into MongoDB
        mongo.db.users.insert_one({'name': name, 'email': email})
        return jsonify({'message': 'Data inserted successfully'}), 200
    else:
        return jsonify({'error': 'Name and email are required'}), 400


if __name__ == '__main__':
    app.run(debug=True)
