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
    # Get the column names
    column_names = ['manufacturer','year', 'condition', 'cylinders', 'fuel', 'odometer', 'transmission','drive', 'type', 'paint_color']
    
    try:
        # Obtain the request parameters
        print(request.form["vehicleType"])
        vehicleType = request.form["vehicleType"] or "truck"
        manufacturer = request.form["carManufacturer"] or "honda" 
        year = request.form["year"] or "2006"
        cylinders = request.form["cylinders"] or "6"
        fuelType = request.form["fuelType"] or "gas"
        odometer = request.form["odometer"] or "30000"
        transmission = request.form["transmission"] or "automatic"
        drive = request.form["drive"] or "rwd"
        condition = request.form["carCondition"] or "good"
        paintColour = request.form["paintColour"] or "red"

        input_data = [manufacturer, year, condition, cylinders, fuelType, odometer, transmission, drive, vehicleType, paintColour]

        print(input_data)
        # Obtain prediction from the model
        input_df = pd.DataFrame(columns=column_names, data=np.array(input_data).reshape(1,10))
                            #   data=np.array(['honda', '2006', 'good', '6', 'gas', '30000', 'automatic','rwd', 'truck', 'red']).reshape(1,10))

        prediction = model.predict(input_df)[0]
    except:
        input_data = ['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA','NA', 'NA', 'NA']
        # If some of the values are not provided, return 0
        prediction = 0

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
        render_template("index.html", prediction = prediction_range, columns = column_names, info = input_data)
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)