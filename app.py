from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pickle
import numpy as np

# Set up flask
app = Flask(__name__)

# Load the machine learning model TODO finalize the pickle file name
#model = pickle.load(open('model.pkl','rb')) 

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
    #vehicleType = request.form["vehicleType"]
    # year = request.form["year"]
    # odometer = request.form["odometer"]
    # fuelType = request.form["fuelType"]
    # condition = request.form["condition"]
    # paintColor = request.form["paintColor"]

    # print("priceInquery is being read okay")
    # print(vehicleType, year, odometer, fuelType, condition, paintColor)
    
    # Obtain prediction from the model
    #prediction = model.predict(
    #    np.array([
    #        vehicleType,
    #        year,
    #        odometer,
    #        fuelType,
    #        condition,
    #        paintColor
    #    ])
    #)

    prediction = [100,400]

    return(
        render_template("index.html", _anchor="facts", prediction = prediction)
        #redirect(url_for('facts', prediction = prediction))
    )


if __name__ == "__main__":
    app.run(debug=True)