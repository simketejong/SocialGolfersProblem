from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# create database connection
conn = sqlite3.connect('golf.db')
c = conn.cursor()

# create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS golfers
             (name TEXT, handicap REAL, email TEXT)''')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get form data
        name = request.form['name']
        handicap = float(request.form['handicap'])
        email = request.form['email']

        # insert into database
        c.execute("INSERT INTO golfers VALUES (?, ?, ?)", (name, handicap, email))
        conn.commit()

    # retrieve golfers from database
    c.execute("SELECT * FROM golfers")
    golfers = c.fetchall()

    # render template with golfers data
    return render_template('index.html', golfers=golfers)

if __name__ == '__main__':
    app.run(debug=True)
