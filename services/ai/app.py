from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Dummy AI model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(["beach", "mountain", "city", "adventure"])
y = ["relax", "nature", "urban", "explore"]
model = LogisticRegression().fit(X, y)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json.get("query", "")
    X_test = vectorizer.transform([data])
    prediction = model.predict(X_test)[0]
    return jsonify({"recommendation": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
