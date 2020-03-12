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
        flag=0
        return flask.render_template("label.html",flag=flag)
    else:
        flag=1
        item_name=flask.request.form.get("item-name").upper()
        model_no=flask.request.form.get("model_no").upper()
        mrp=flask.request.form.get("mrp").upper()
        offerpr=flask.request.form.get("offerpr").upper()
       
        new_lb = Tag(item_name=item_name,model_no=model_no,mrp=mrp,offer_pr=offerpr)
        error=""
        if not item_name:
            error="ITEM NAME"
            return flask.render_template("error.html",error=error)
        if not model_no:
            error="MODEL NUMBER"
            return flask.render_template("error.html",error=error)
        if not mrp:
            error="MRP"
            return flask.render_template("error.html",error=error)
        if not offerpr:
            error="OFFER PRICE"
            return flask.render_template("error.html",error=error)
        db.session.add(new_lb)
        db.session.commit()
        return flask.render_template("label.html",flag=flag)
       


@app.route("/page")
def page():
    info=Tag.query.all()
    return flask.render_template("page.html",info=info)
