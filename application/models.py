from . import db

class Farmers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    farm = db.Column(db.String(30), unique = True, nullable = False)
    age = db.Column(db.Integer)
    good = db.relationship('Goods', backref='farmers', lazy=True)

class Goods(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    equipment = db.Column(db.String(30), nullable = False)
    equipmenttype = db.Column(db.String(30), nullable = False)
    vegetables = db.Column(db.String(30), nullable = False)
    vegenum = db.Column(db.Integer, nullable = False)
    fruits = db.Column(db.String(30), nullable = False)
    fruitnum = db.Column(db.Integer)
    farmers_id = db.Column(db.Integer, db.ForeignKey('farmers.id'), nullable=False)