from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('songs.json', 'r', encoding='utf-8') as f:
        songs = json.load(f)
    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
