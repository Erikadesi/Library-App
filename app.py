from flask import Flask, render_template, send_file, request
import pandas as pd  
from io import BytesIO

app = Flask(__name)

# Sample data
users = [
    {"nama": "Rika", "email": "Rika@example.com"},
    {"nama": "Usna", "email": "Usna@example.com"}
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        users.append({"nama": nama, "email": email})
        return redirect(url_for('home'))
    
    return render_template('index.html', users=users)

@app.route('/about')
def about():
    app_info = {
        "nama_aplikasi": "Flask Demo",
        "versi": "1.0",
        "pembuat": "Anda"}
    return render_template('about.html', info=app_info)

@app.route('/hapus-user/<int:user_id>')
def hapus_user(user_id):
    if 0 <= user_id < len(users):
        users.pop(user_id)
    return redirect(url_for('home'))

if __name == '__main__':
    app.run()