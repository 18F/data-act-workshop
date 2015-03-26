import os

from flask import Flask
from flask import render_template

import validator

app = Flask(__name__)

test_data = {
  'agency': 'FWS',
  'currentAmount': 500,
  'initialAmount': 1000,
  'outlays': 500
}

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/submission/validation")
def validation():
    data = test_data
    errors = validator.validate(data)
    context = {
        'errors': errors
    }
    return render_template('validation.html', context=context)

if __name__ == "__main__":

    port = os.getenv('VCAP_APP_PORT', '5000')

    app.config['DEBUG'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(port=int(port), host='0.0.0.0')
