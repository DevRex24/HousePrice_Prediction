from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "house_price_model.pkl")

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def price():
    prediction = None
    error = None
    if request.method == "POST":
        try:
            size = float(request.form["size"])

            if size <= 0:
                error = "House size must be a positive number"
            elif size > 10000:
                error = "House size seems too large (max 10,000 sq ft)"
            else:
                x = pd.DataFrame([[size]], columns=["Size"])
                prediction = float(model.predict(x)[0])

                prediction = round(prediction, 2)
        except ValueError:
            error = "Please enter a valid number for house size"
        except Exception as e:
            print("Prediction error:", e)
            error = "An error occurred during prediction: " + str(e)
    
    return render_template("form.html", prediction=prediction, error=error)

@app.route("/predict", methods=["POST"])
def predict_api():
    try:
        data = request.get_json()
        size = float(data["size"])
        
        if size <= 0:
            return jsonify({"error": "House size must be a positive number"}), 400
        elif size > 10000:
            return jsonify({"error": "House size seems too large (max 10,000 sq ft)"}), 400
            
        x = pd.DataFrame([[size]], columns=["Size"])
        prediction = float(model.predict(x)[0])
        
        return jsonify({
            "prediction": round(prediction, 2),
            "formatted_prediction": f"₹{prediction:,.2f}",
            "note": "Prices are in Indian Rupees (₹)"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=1234)