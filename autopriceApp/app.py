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
import pandas as pd

# Set up flask
app = Flask(__name__)

# Load the model
f = gzip.open('autopriceApp/model/new_car_prediction_compressed.pkl','rb')
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
    paintColour = request.form["paintColour"]

    input_data = [manufacturer, year, condition, cylinders, fuelType, odometer, transmission, drive, vehicleType, paintColour]

    print(input_data)
    # Obtain prediction from the model

    input_df = pd.DataFrame(columns=['manufacturer','year', 'condition', 'cylinders', 'fuel', 'odometer', 'transmission','drive', 'type', 'paint_color'],
                          data=np.array(input_data).reshape(1,10))
                        #   data=np.array(['honda', '2006', 'good', '6', 'gas', '30000', 'automatic','rwd', 'truck', 'red']).reshape(1,10))

    prediction = model.predict(input_df)[0]

    # round prediction value to obtain price range 
    def roundup(x):
        return int(math.ceil(x / 1000)) * 1000

    def rounddown(x):
        return int(math.floor(x/1000))*1000

    # prediction = prediction #fake value for testing purpose
    prediction_range = [0, 0] #placeholder for ranges
    prediction_range[0] = rounddown(prediction) 
    prediction_range[1] = roundup(prediction)

    print(prediction)
    print(prediction_range)

    return(
        render_template("index.html", prediction = prediction_range)
    )


if __name__ == "__main__":
    app.run(debug=True)