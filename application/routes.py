from flask import redirect, url_for, request, render_template
from . import app
from . import db
from .models import Farmers, Goods
from .forms import Farmform
#Defaults both tables on default application route and home route shows Read route
@app.route('/')
@app.route('/home')
def home():
    farmers = Farmers.query.all()
    good = Goods.query.all()
    return render_template('home.html', farmers=farmers, good=good)

#Route for adding new entries to table
@app.route("/create", methods=['GET', 'POST']) 
def create():
    new = Farmform()
    if request.method == 'POST':
        new_farmer = Farmers(
            name = new.name.data,
            farm = new.farm.data,
            age = new.age.data
        )
        db.session.add(new_farmer)
        db.session.commit()
    #Splitting all data acquired
        equip = new.equipment.data
        equip_split = equip.split(",")
        equipt = new.equipmenttype.data
        equipt_split = equipt.split(",")
        vege = new.vegetables.data
        vege_split = vege.split(",")
        vegen = new.vegenum.data
        vegen_split = list(map(int,vegen.split(",")))
        fruit = new.fruits.data
        fruit_split = fruit.split(",")
        fruitn = new.fruitnum.data
        fruitn_split = list(map(int,fruitn.split(",")))
        
        #Adding all split elements into database
        for i in range(0, len(equip_split)):

            entry = equip_split[i]

            new_comp = Goods(equipment = entry, farmers_id=new_farmer.id)

            db.session.add(new_comp)
            

        for i in range(0, len(equipt_split)):

            entry = equipt_split[i]

            new_comp = Goods(equipmenttype = entry, farmers_id=new_farmer.id)

            db.session.add(new_comp)
            
        
        for i in range(0, len(vege_split)):

            entry = vege_split[i]

            new_comp = Goods(vegetables = entry, farmers_id=new_farmer.id)

            db.session.add(new_comp)
            

        for i in range(0, len(vegen_split)):

            entry = vegen_split[i]

            new_comp = Goods(vegenum = entry, farmers_id=new_farmer.id)

            db.session.add(new_comp)
            

        for i in range(0, len(fruit_split)):

            entry = fruit_split[i]

            new_comp = Goods(fruits = entry, farmers_id=new_farmer.id)

            db.session.add(new_comp)
            
        
        for i in range(0, len(fruitn_split)):

            entry = fruitn_split[i]

            new_comp = Goods(fruitnum = entry, farmers_id=new_farmer.id)

            db.session.add(new_comp)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("create.html", new = new)
#Update route for changing values in the database       
@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):

    #Access to all farmers with the specific ID
    farms = Farmers.query.get(id)
    new = Farmform()
    if new.validate_on_submit():
        
        farms.name=new.name.data
        farms.farm=new.farm.data
        farms.age=new.age.data
        db.session.add(farms)  
        db.session.commit()

        equip = new.equipment.data
        equip_split = equip.split(",")
        equipt = new.equipmenttype.data
        equipt_split = equipt.split(",")
        vege = new.vegetables.data
        vege_split = vege.split(",")
        vegen = new.vegenum.data
        vegen_split = list(map(int,vegen.split(",")))
        fruit = new.fruits.data
        fruit_split = fruit.split(",")
        fruitn = new.fruitnum.data
        fruitn_split = list(map(int,fruitn.split(",")))

        #Finds all entries for the ID
        all = Goods.query.filter_by(farmers_id = id).all()

        #Deletes all of the found entries
        for entry in all:
            db.session.delete(entry)
        
        #Updating all split elements into database
        for i in range(0, len(equip_split)):

            entry = equip_split[i]

            new_comp = Goods(equipment = entry, farmers_id=id)

            db.session.add(new_comp)
            

        for i in range(0, len(equipt_split)):

            entry = equipt_split[i]

            new_comp = Goods(equipmenttype = entry, farmers_id=id)

            db.session.add(new_comp)
            
        
        for i in range(0, len(vege_split)):

            entry = vege_split[i]

            new_comp = Goods(vegetables = entry, farmers_id=id)

            db.session.add(new_comp)
            

        for i in range(0, len(vegen_split)):

            entry = vegen_split[i]

            new_comp = Goods(vegenum = entry, farmers_id=id)

            db.session.add(new_comp)
            

        for i in range(0, len(fruit_split)):

            entry = fruit_split[i]

            new_comp = Goods(fruits = entry, farmers_id=id)

            db.session.add(new_comp)
            
        
        for i in range(0, len(fruitn_split)):

            entry = fruitn_split[i]

            new_comp = Goods(fruitnum = entry, farmers_id=id)

            db.session.add(new_comp)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("create.html", new = new)

#Delete route created
@app.route("/delete/<int:id>")
def delete(id):

    farm = Farmers.query.get(id)
    good = Goods.query.all()

    #Removes the required entry in farmers
    db.session.delete(farm)
    
    #Goes through the Goods table to remove any values related to the foreign key
    for entry in good:
        if entry.farmers_id == id:
            db.session.delete(entry)

    db.session.commit()
    return redirect(url_for("home")) 
        