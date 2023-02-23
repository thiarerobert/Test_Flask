from flask import Flask, url_for, request, render_template, redirect
import sqlite3
from flask import g
from markupsafe import escape

app = Flask(__name__)
app.config['SECRET_KEY'] = "FDJOIWTW938123459-FK234@014!DLpdgw-432049"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/enregistrer', methods = ('GET', 'POST'))
def home():
    return render_template('login.html')

@app.route("/enregistrer/", methods=['GET', 'POST'])
def enregistrer():
    if request.method == 'POST':

            pm = request.form['pm']
            nm = request.form['nm']
            cl = request.form['cl']
            ad = request.form['ad']
            pr = request.form['pr']
            tl = request.form['tl']
            vl = request.form['vl']
            cp = request.form['cp']

            print("les données: "+ pm, " | ", nm, " | ", cl, " | ", ad, " | ", pr, " | ", tl," | ", vl," | ",cp);

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (prenom, nom, courriel, adresse, province, telephone, ville, codePostal) VALUES (?,?,?,?,?,?,?,?)", (pm,nm,cl,ad,pr,tl,vl,cp))
            conn.commit()
            conn.close()
    return redirect(url_for('result.html'))




if __name__ == '__main__':
    app.run(debug = True)