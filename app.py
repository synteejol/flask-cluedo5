from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from tabledef import *

import dummy








engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
admin = User(username='admin', password='password')
db.session.add(admin)
db.session.commit()

# @app.route('/test')
# def test():
#
#     POST_USERNAME = "python"
#     POST_PASSWORD = "python"
#
#     Session = sessionmaker(bind=engine)
#     s = Session()
#     User.query.all()
#     result=User.query.filter_by(username='admin').first()
#     #query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
#     #result = query.first()
#     if result:
#         return "Object found"
#     else:
#         return "Object not found " + POST_USERNAME + " " + POST_PASSWORD


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href=/logout>Logout</a>"

@app.route('/login', methods=['POST'])
def do_admin_login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    User.query.all()
    result=User.query.filter_by(username='admin').all()
    #query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    #result = query.first()
    if result:
        session['logged_in'] = True
        #return render_template("/Enigma2")
        return redirect(url_for('enigma2'))
    else:
        flash('wrong password!')
        #return render_template("/login")
        return redirect(url_for('login'))
    #return enigma2()



@app.route("/Enigma2", methods=["GET", "POST"])

def enigma2():
        if not session.get('logged_in'):
            return render_template('login.html')
        else:

            session['logged_in_2'] = False
            if request.method == 'POST':

                password = request.form['password_en']

                if password == "ciao":

                    session['logged_in_2'] = True
                    if request.form['action'] == 'Submit':
                        return redirect(url_for('enigma3'))
                    # return redirect(request.args.get("next"))
                else:

                    return abort(401)
            else:

                return render_template('Enigma2.html')

@app.route("/Enigma3", methods=["GET", "POST"])

def enigma3():
    if not session.get('logged_in_2'):
        return render_template('login.html')
    else:

        session['logged_in_3'] = False
        if request.method == 'POST':

            password = request.form['password_en']

            if password == "ciao":

                session['logged_in_3'] = True
                if request.form['action'] == 'Submit':
                    return redirect(url_for('enigma4'))
                # return redirect(request.args.get("next"))
            else:

                return abort(401)
        else:

            return render_template('Enigma3.html')

@app.route("/Enigma4", methods=["GET", "POST"])
def enigma4():
    if not session.get('logged_in_3'):
        return render_template('login.html')
    else:

        session['logged_in_4'] = False
        if request.method == 'POST':

            password = request.form['password_en']

            if password == "ciao":

                session['logged_in_4'] = True
                if request.form['action'] == 'Submit':
                    return redirect(url_for('enigma5'))
                # return redirect(request.args.get("next"))
            else:

                return abort(401)
        else:

            return render_template('Enigma4.html')

@app.route("/Enigma5", methods=["GET", "POST"])
def enigma5():
    if not session.get('logged_in_3'):
        return render_template('login.html')
    else:

        session['logged_in_4'] = False
        if request.method == 'POST':

            password = request.form['password_en']

            if password == "ciao":

                session['logged_in_4'] = True
                if request.form['action'] == 'Submit':
                    return redirect(url_for('enigma5'))
                # return redirect(request.args.get("next"))
            else:

                return abort(401)
        else:

            return render_template('Enigma5.html')







@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)