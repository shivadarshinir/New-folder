import flask
from flask import Flask, render_template
app = flask.Flask(__name__)

@app.route("/")

@app.route('/signup')
def index():
    
    return flask.render_template("signup.html")

@app.route('/index')
def plots():
    return render_template('index.html')

@app.route('/webpage')
def plots():
    return render_template('webpage.html')


@app.route('/blogContent')
def heatmaps():
    return render_template('blogContent.html')

@app.route('/login')
def heatmaps():
    return render_template('login.html')

@app.route('/creat-blog')
def heatmaps():
    return render_template('blogForm.html')




app.run(debug=True)