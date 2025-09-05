from flask import Flask, request, jsonify
import pickle, pandas as pd
from feature_utils import extract_features  # keep your feature function separate

# Load model
with open("rf_url_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "API is running 🚀"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "URL missing"}), 400

    # Extract features
    feats = extract_features(url)
    X = pd.DataFrame([feats])

    # Predict
    pred = model.predict(X)[0]
    proba = model.predict_proba(X).max()

    return jsonify({
        "url": url,
        "prediction": str(pred),
        "confidence": float(round(proba, 4))
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
