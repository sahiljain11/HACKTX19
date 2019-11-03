from flask import Flask, request
import flask
from flask import Flask, flash, request, redirect, url_for, session
from find_damaged import *
import json
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import io
from flask import jsonify

app = Flask(__name__)

UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def fileUpload():
	file = request.files['0'] 
	file.save('react-front-end/public/images/uploaded.png')
	filename = 'react-front-end/public/images/uploaded.png'
	find_damage(filename).save('react-front-end/public/images/wassup.png')
	return 'hi'

@app.route("/")
def hello():
	return flask.render_template("index.html", token="Hello Flask+React")

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    session.init_app(app)
    app.run(use_reloader=False)

@app.route("/react-front-end/public/images/wassup.png")
def hey():
	return flask.send_file("/react-front-end/public/images/wassup.png")