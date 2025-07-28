from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('songs.json', 'r', encoding='utf-8') as file:
        songs = json.load(file)
    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
    