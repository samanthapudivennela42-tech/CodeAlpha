from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

connection = psycopg2.connect(
    "postgresql://neondb_owner:npg_2voKInBe7yOV@ep-rough-boat-atho3cti-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

cursor = connection.cursor()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():

    data = request.get_json()

    stock = data["stock"]
    quantity = data["quantity"]
    price = data["price"]

    cursor.execute(
        "INSERT INTO portfolio(stock_name, quantity, price) VALUES(%s, %s, %s)",
        (stock, quantity, price)
    )

    connection.commit()

    return jsonify({
        "message":"Stock Added Successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)