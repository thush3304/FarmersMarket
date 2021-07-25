from application import db
from application.models import Farmers,Goods

#Initialises a new database by removing any previous databases
db.drop_all()
db.create_all()

#Creates Farmers Entry
farm1 = Farmers(
    name = "Kesh",
    farm = "Sunflower",
    age = 20
)
farm2 = Farmers(
    name = "Thush",
    farm = "Lavender",
    age = 22
)
#Creates goods entry in relation to farm1
good = Goods(
    equipment = "Tractor",
    equipmenttype = "Vehicle",
    vegetables = "Sawi",
    vegenum = 20,
    fruits = "Mango",
    fruitnum = 55,
    farmers_id = 1,
)
good2 = Goods(
    equipment = "",
    equipmenttype = "",
    vegetables = "Chillies",
    vegenum = 123,
    fruits = "Durian",
    fruitnum = 64,
    farmers_id = 1,
)
#goods addition for farmer2
good3 = Goods(
    equipment = "Fork",
    equipmenttype = "Tools",
    vegetables = "Celery",
    vegenum = 18,
    fruits = "Apples",
    fruitnum = 5,
    farmers_id = 2,
)

good4 = Goods(
    equipment = "Spade",
    equipmenttype = "Tools",
    vegetables = "Lettuce",
    vegenum = 10,
    fruits = "Oranges",
    fruitnum = 23,
    farmers_id = 2
)
#Adds all changes onto the database
db.session.add(farm1)
db.session.add(farm2)
db.session.add(good)
db.session.add(good2)
db.session.add(good3)
db.session.add(good4)

#Commits all changes onto database
db.session.commit()
