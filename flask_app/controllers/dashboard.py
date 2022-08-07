from crypt import methods
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.dashboard import Message
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact/alex', methods=['POST'])
def contact_alex():
    data = {
        "contact": request.form["contact"],
        "message": request.form["message"],
    }
    Message.save(data)
    return redirect('/')