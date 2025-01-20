import os

# Module de connexion à la base de données (sqlite locale pour le projet)
import sqlite3

from flask import Flask, render_template

app = Flask(__name__)

# Chemin absolu du répertoire où se trouve main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template('index.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
