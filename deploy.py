from flask import Flask
from flask import jsonify
from flask import render_template
import MySQLdb

app = Flask(__name__)

@app.route("/")
def index_void():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/login.html")
def login():
    return render_template('login.html')

@app.route("/mainpage.html")
def mainpage():
    return render_template('mainpage.html')

@app.route("/imagelabel.html")
def imagelabel():
    return render_template('imagelabel.html')

@app.route("/publish.html")
def publish():
    return render_template('publish.html')

@app.route("/textlabel.html")
def textlabel():
    return render_template('textlabel.html')

@app.route("/textlabel2.html")
def textlabel2():
    return render_template('textlabel2.html')

@app.route('/test1')
def summary():
    return jsonify("a")

@app.route('/login/username/<user_name>/password/<pass_word>')
def verification(user_name, pass_word):
    conn = MySQLdb.connect(host='127.0.0.1',user="root",passwd="se2018",db="se_proj")
    cur = conn.cursor()
    cur.execute('select * from users;')
    print("aaa")
    for row in cur:
        if row[1] == user_name:
            if row[2] == pass_word:
                verification = {'code':0}
            elif row[2] != pass_word:
                verification = {'code':1}
    return jsonify(verification)