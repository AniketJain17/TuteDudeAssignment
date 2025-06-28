
from flask import Flask, request, redirect, render_template_string
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["mydatabase"]   # Uses default DB from URI
collection = db['form_data']

@app.route('/', methods=['GET'])
def index():
    return render_template_string(open('../frontend/index.html').read(), error='')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        if not name or not email:
            raise ValueError("Name and Email are required")
        collection.insert_one({'name': name, 'email': email})
        return redirect('/success')
    except Exception as e:
        return render_template_string(open('../frontend/form.html').read(), error=str(e))

@app.route('/success', methods=['GET'])
def success():
    return render_template_string(open('../frontend/success.html').read())

if __name__ == '__main__':
    app.run(debug=True)
