from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/customers", methods=["GET"])
def get_customers():
    customers = [
        {"name": "Febin", "premium_customer": True},
        {"name": "Cristiano", "premium_customer": True},
        {"name": "Messi", "premium_customer": True},
        {"name": "Neymar", "premium_customer": False}
    ]

    return jsonify({
        "customers": customers
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

