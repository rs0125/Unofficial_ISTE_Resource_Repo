from flask import Flask, render_template
from static import *

app = Flask(__name__)




@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="The Unofficial ISTE Resource Repository")

@app.route("/design")
def design():
    return render_template("display.html", title="Design", resources=design_res)

@app.route("/web")
def webdev():
    return render_template("display.html", title="Web Development", resources=web_res)

@app.route("/app")
def appdev():
    return render_template("display.html", title="App Development", resources=app_res)


@app.route("/aiml")
def aiml():
    return render_template("wip.html", title="AI/ML")

@app.route("/motiongraphics")
def motion():
    return render_template("wip.html", title="Motion Graphics")


if __name__ == '__main__':
    app.run(debug=True)
