
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    
    port = os.getenv('PORT', '5000')
    
    app.run(port=int(port), host='0.0.0.0')
