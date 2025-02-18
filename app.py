from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Serve the HTML file at the root URL
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True) 