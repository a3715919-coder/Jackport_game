from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Random Jackpot Number
jackpot = random.randint(1, 100)
print("Jackpot Number:", jackpot)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        guess = int(request.form["guess"])

        if guess == jackpot:
            result = "🎉 Congratulations! You Won."

        elif guess < jackpot:
            result = "⬆️ Guess Higher Number"

        else:
            result = "⬇️ Guess Lower Number"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
