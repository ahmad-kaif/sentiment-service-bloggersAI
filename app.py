from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Welcome to the Sentiment Analyzer!"


@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.json
    content = data.get("text", "")
    
    blob = TextBlob(content)
    polarity = blob.sentiment.polarity

    return jsonify({ "polarity": polarity })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

