from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://database:27017/")
db = client["webappdb"]
collection = db["users"]

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    user_data = {"name": name, "email": email}
    collection.insert_one(user_data)
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
