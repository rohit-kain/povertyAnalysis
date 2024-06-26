from flask import Flask, render_template, request, jsonify
import os


app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        template_name_or_list="views/dashboard.html",
        page="dash",
        title="Dashboard - Explore the Dataset",
    )


@app.route("/predict")
def predict():
    return render_template(
        template_name_or_list="views/predict.html",
        page="predict",
        title="Predict Wealth Index",
    )


@app.route("/g")
def g():
    wealthIdx = -1
    if len(request.files):
        ...
        # Predict using image
    elif len(request.args):
        waterSourceDistance = request.args.get["waterSourceDistance"]
        elecAvailability = request.args.get["elecAvailability"]
        cellAccess = request.args.get["cellAccess"]
        educatedInYear = request.args.get["educatedInYear"]
        # prediction = model.predict(waterSourceDistance, elecAvailability, cellAccess, educatedInYear)
        #? Process prediction variable
        # wealthIdx = prediction
        ...
        # Predict using form data
    return jsonify(estimated_wealth_index=wealthIdx)


if __name__ == "__main__":
    #app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0', port=port)
