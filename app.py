from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message="Full CICD!")

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(received=data)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
