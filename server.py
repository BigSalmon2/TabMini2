from flask import Flask, request, Response, render_template, jsonify
import requests
import time
import random

app = Flask(__name__, static_url_path='/static')

models = {
    "gpt2-story": "https://main-flowberta-big-salmon2.endpoint.ainize.ai/gpt2-story",
    "gpt2-cover-letter": "http://main-gpt2-cover-letter-jeong-hyun-su.endpoint.ainize.ai/gpt2-cover-letter/long",
    "gpt2-reddit": "https://main-flowberta-big-salmon2.endpoint.ainize.ai/gpt2-story/long",
}

@app.route("/gpt2", methods=["POST"])
def gpt2():
    context = request.form['context']
    model = request.form['model']
    length = request.form['length']

    url = models[model]

    if length == "short":
        length = random.randrange(2,6)
    else:
        length = 3
    
    data = {
        "text": context,
        "num_samples": 5,
        "length": 3,
        "model": "BigSalmon/Flowberta"
    }

    response = requests.post(url, data=data)
    res = response.json()
    
    return res


@app.route("/")
def main():
    return render_template("index.html")


# Health Check
@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)   
