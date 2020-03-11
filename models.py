from application import db

class Tag(db.Model):
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(256), nullable=False)
    model_no = db.Column(db.String(256), nullable=False)
    mrp = db.Column(db.Integer, nullable=False)
    offer_pr= db.Column(db.String(256), nullable=False)

