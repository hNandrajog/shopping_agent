
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load static product memory (replace with DB later)
with open("product_db.json", "r") as f:
    PRODUCT_DB = json.load(f)

def match_product(user_input):
    user_input = user_input.lower()
    for keyword, url in PRODUCT_DB.items():
        if keyword in user_input:
            return url
    return None

@app.route("/query", methods=["POST"])
def handle_query():
    data = request.json
    user_input = data.get("message", "")
    product_link = match_product(user_input)
    if product_link:
        return jsonify({"status": "success", "link": product_link})
    else:
        return jsonify({"status": "not_found", "message": "No matching product found."})

@app.route("/ping", methods=["GET"])
def ping():
    return "Server is up!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
