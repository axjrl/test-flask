from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    information = {
        "name" : "Ilja Dikteriov",
        "date" : "Sep 30, 2003",
        "phone" : "+37063033080",
        "email" : "axjrl.i.d@gmail.com",
        "priceReact" : "200",
        "priceDesign" : "50"
    }
    return render_template("index.html", information = information)