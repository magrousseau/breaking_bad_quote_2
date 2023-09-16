from flask import Flask, jsonify, render_template
from quote import breaking_quote

app = Flask(__name__)


#homepage endpoint
@app.route("/")
def index():
    return render_template('index.html')


#quote endpoint
@app.route("/quote")
def quote():
  random_quote = breaking_quote()
  return jsonify({"quote": random_quote})


#this part is executed when the module is called directly - "pipenv run python app.py"
if __name__ == "__main__":
    app.run(debug=True)
