from flask import render_template, redirect
from flask_app import app

@app.route('/play')
def play():
    return render_template('dashboard.html', num = 3)


@app.route('/play/<int:numriKutive>')
def playWithBoxes(numriKutive):
    return render_template('dashboard.html', num = numriKutive)

@app.route('/play/<int:numriKutive>/<color>')
def playWithBoxesAndColors(numriKutive, color):
    return render_template('dashboard.html', num = numriKutive, color = color)