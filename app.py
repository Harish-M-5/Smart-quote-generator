from flask import Flask

app = Flask(__name__)

quotes = [
    "Believe in yourself, success will follow.",
    "Hard work beats talent when talent doesn’t work hard.",
    "Small steps every day lead to big achievements.",
    "Focus on progress, not perfection.",
    "Discipline is the bridge between goals and success."
]

@app.route("/")
def home():
    return "Welcome to Smart Quote Generator API! Use /quote to get a motivational quote."

@app.route("/quote")
def get_quote():
    import random
    return f"Motivational Quote: {random.choice(quotes)}"

if __name__ == "__main__":
    app.run(debug=True)

