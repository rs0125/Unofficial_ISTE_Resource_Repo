from flask import Flask, render_template
from static import *

app = Flask(__name__)




@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="The Unofficial Resource Repo")

@app.route("/design")
def design():
    return render_template("design.html", title="Design & Motion Graphics", resources=design_res)

@app.route("/web")
def webdev():
    return render_template("web.html", title="Web Development", resources=web_res)

@app.route("/app")
def appdev():
    return render_template("app.html", title="App Development", resources=app_res)

if __name__ == '__main__':
    app.run(debug=True)
