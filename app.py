from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load song data from JSON file
with open("songs.json", "r", encoding="utf-8") as f:
    songs = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", songs=songs)

@app.route("/api/songs")
def get_songs():
    return jsonify(songs)

if __name__ == "__main__":
    app.run(debug=True)
# app.py - Flask application for BTS song site
# This file sets up the Flask app, loads song data from a JSON file,    