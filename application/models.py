from . import db
#creates table farmers with columns
class Farmers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    farm = db.Column(db.String(30), unique = True, nullable = False)
    age = db.Column(db.Integer)
    good = db.relationship('Goods', backref='farmers', lazy=True)
#creates table goods with columns and foreign key
class Goods(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    equipment = db.Column(db.String(30), nullable = True)
    equipmenttype = db.Column(db.String(30), nullable = True)
    vegetables = db.Column(db.String(30), nullable = True)
    vegenum = db.Column(db.Integer, nullable = True)
    fruits = db.Column(db.String(30), nullable = True)
    fruitnum = db.Column(db.Integer)
    farmers_id = db.Column(db.Integer, db.ForeignKey('farmers.id'), nullable=False)