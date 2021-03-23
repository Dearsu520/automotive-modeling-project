from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

## Set up flask
app = Flask(__name__)

## Route to the landing page
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)