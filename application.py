import flask
import flask_sqlalchemy
import flask_migrate


# Initializes the app
app = flask.Flask(__name__)

#configuers the app
from config import Config
app.config.from_object(Config)

#Sets up Database
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

# imports everything from models 
from models import *

#routes
@app.route("/")
def index():
    Tag.query.delete()
    db.session.commit()
    return flask.render_template("index.html")

@app.route("/label",methods=["POST","GET"])
def Label():
    if flask.request.method =="GET":
        return flask.render_template("label.html")
    else:
        item_name=flask.request.form.get("item-name")
        model_no=flask.request.form.get("model_no")
        mrp=flask.request.form.get("mrp")
        offerpr=flask.request.form.get("offerpr")
        print(item_name,model_no,mrp,offerpr)
        new_lb = Tag(item_name=item_name,model_no=model_no,mrp=mrp,offer_pr=offerpr)
        db.session.add(new_lb)
        db.session.commit()
        return flask.render_template("label.html")



