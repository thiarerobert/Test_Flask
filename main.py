from flask import Flask, url_for, request, render_template, redirect
import sqlite3
from flask import g
from markupsafe import escape

app = Flask(__name__)
app.config['SECRET_KEY'] = "FDJOIWTW938123459-FK234@014!DLpdgw-432049"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn


"""Route racine pour la page d'accueil"""
@app.route('/')
def index():
    return render_template('home.html')

"""Route pour accèder au formulaire de création d'un utilisateur"""
@app.route('/enregistrer', methods = ('GET', 'POST'))
def home():
    return render_template('login.html')

"""Route pour accéder aux utlisateurs ajoutés"""
@app.route("/utilisateurs", methods = ['GET'])
def getUtilisateur():
    con = get_db_connection()
    con.row_factory = sqlite3.Row

    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall();
    return render_template('utilisateur.html', users = users)

"""Route pour créer un utilisateur"""
@app.route("/enregistrer/", methods=['GET', 'POST'])
def enregistrer():
    if request.method == 'POST':
        try:
            pm = request.form['pm']
            nm = request.form['nm']
            cl = request.form['cl']
            ad = request.form['ad']
            pr = request.form['pr']
            tl = request.form['tl']
            vl = request.form['vl']
            cp = request.form['cp']

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (prenom, nom, courriel, adresse, province, telephone, ville, codePostal) VALUES (?,?,?,?,?,?,?,?)", (pm,nm,cl,ad,pr,tl,vl,cp))
            conn.commit()
            msg = "utilisateur créé avec succès"

        except:
            conn.rollback()
            msg = "Erreur lors de l'envoie"

        finally:
            return render_template("result.html", msg = msg)
            conn.close()


if __name__ == '__main__':
    app.run(debug = True)