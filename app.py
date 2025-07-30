from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Stay hungry. Stay foolish.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "In a world full of trends, I want to remain a classic.",
    "Consistency is more important than perfection."
]

@app.route('/')
def random_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)

