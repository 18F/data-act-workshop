import os

from flask import Flask
from flask import render_template, request, redirect, url_for
from flask import send_from_directory
from werkzeug import secure_filename

import csv_reader
import validator

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
CSV_LOCATION = 'uploads/data.csv'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/submission/validation")
def validation():
    data = csv_reader.read_csv(CSV_LOCATION)
    errors = validator.validate(data)
    context = {
        'errors': errors
    }
    return render_template('validation.html', context=context)

@app.route("/submission/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        datafile = request.files['file']
        filename = secure_filename(datafile.filename)
        datafile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('upload.html',
                               status='complete',
                               filename=filename)
        datafile.save(os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv'))
        return render_template('upload.html', status='complete')
    return render_template('upload.html', status='incomplete')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":

    port = os.getenv('VCAP_APP_PORT', '5000')

    app.config['DEBUG'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(port=int(port), host='0.0.0.0')
