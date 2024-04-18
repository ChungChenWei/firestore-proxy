from flask import Flask, render_template, request

import firestore as db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/token", methods=["POST", "GET"])
def update_token():
    if request.method == "POST":
        token = request.form.get("token", None)
        if token:
            try:
                db.update_token(token)
                return {"message": "success"}, 200
            except Exception:
                return {"message": "failed"}, 500
        return {"message": "failed"}, 400
    elif request.method == "GET":
        device_id = request.args.get("device_id", None)
        if device_id:
            try:
                token = db.fetch_token(device_id)
                return {"token": token}, 200
            except Exception:
                return {"message": "failed"}, 500
        return {"message": "failed"}, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
