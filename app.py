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

## Route to show available APIs
@app.route("/api")
def api():
    return ("<ul>" +
    "<li><p3>/: Landing page</p3></li>" + 
    "<li><p3>/home: Landing page</p3></li>" +
    "<li><p3>/api: page to show all the APIs</p3></li>" +
    "<li>/api/priceInquery: Route to send and receive inqueries and results</p3></li>"
    "</ul>")

## Route for posting user inqueries
@app.route("/api/priceInquery", methods=["GET", "POST"])
def priceInquery():
    if request.method == "POST":
        vehicleType = request.form["vehicleType"]
        model = request.form["model"]
        year = request.form["year"]
        fuelType = request.form["fuelType"]
        condition = request.form["condition"]
        paintColor = request.form["paintColor"]

    ## TODO: The machine learning model needs to be loaded to finish this
    return jsonify({"message": "Model will be loaded shortly"}), 200

if __name__ == "__main__":
    app.run(debug=True)