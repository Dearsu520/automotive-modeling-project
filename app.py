from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pickle
import gzip
import numpy as np
import math 

# Set up flask
app = Flask(__name__)

# Load the model
f = gzip.open('ETL/new_car_prediction_compressed.pkl','rb')
model = pickle.load(f)

# Route to the landing page
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# Route to show available APIs
@app.route("/api")
def api():
    return ("<ul>" +
    "<li><p3>/: Landing page</p3></li>" + 
    "<li><p3>/home: Landing page</p3></li>" +
    "<li><p3>/api: page to show all the APIs</p3></li>" +
    "<li><p3>/api/priceInquery: Route to send and receive inqueries and results</p3></li>"
    "</ul>")


# Route for posting user inqueries
@app.route("/api/priceInquery", methods=["POST", "GET"])

def priceInquery():

    # Obtain the request parameters
    print(request.form)
    vehicleType = request.form["vehicleType"]
    manufacturer = request.form["carManufacturer"]
    year = request.form["year"]
    cylinders = request.form["cylinders"]
    fuelType = request.form["fuelType"]
    odometer = request.form["odometer"]
    transmission = request.form["transmission"]
    drive = request.form["drive"]
    condition = request.form["carCondition"]
    paintColor = request.form["paintColour"]

   
    # Obtain prediction from the model

    # ['manufacturer','year', 'condition', 'cylinders', 'fuel', 'odometer', 'transmission','drive', 'type', 'paint_color']

    # prediction = model.predict(
    #    np.array([
    #        vehicleType,
    #        year,
    #        odometer,
    #        fuelType,
    #        condition,
    #        paintColor
    #    ])
    # )

 

    # round prediction value to obtain price range 
    def roundup(x):
        return int(math.ceil(x / 1000)) * 1000

    def rounddown(x):
        return int(math.floor(x/1000))*1000

    prediction = 132321 #fake value for testing purpose
    prediction_range = [0, 0] #placeholder for ranges
    prediction_range[0] = rounddown(prediction) 
    prediction_range[1] = roundup(prediction)

    return(
        render_template("index.html", prediction = prediction_range)
    )


if __name__ == "__main__":
    app.run(debug=True)