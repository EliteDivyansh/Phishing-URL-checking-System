# app.py
from flask import Flask, request, render_template
from feature import FeatureExtraction

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url", "").strip()
        fe = FeatureExtraction(url)
        safe_prob = fe.score()  # 0..1
        return render_template("index.html", xx=float(safe_prob), url=url)
    return render_template("index.html", xx=-1, url="")

if __name__ == "__main__":
    app.run(debug=True)
