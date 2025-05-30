from flask import Flask, render_template, send_from_directory
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/geojson")
def geojson():
    return send_from_directory("static/data","data_penyakit_per100k_clustered.geojson")

if __name__ == "__main__":
    app.run(debug=True)