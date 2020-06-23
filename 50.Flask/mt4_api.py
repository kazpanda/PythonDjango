# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def root():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
    