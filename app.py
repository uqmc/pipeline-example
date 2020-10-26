from flask import Flask

app = Flask(__name__)


@app.route("/")
def serve():
    value = 1
    return f"Hello world {value}"

app.run(host="0.0.0.0", port=3000)