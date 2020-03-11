import flask


# Initializes the app
app = flask.Flask(__name__)

#routes
@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/Label")
def Label():
    return flask.render_template("label.html")
