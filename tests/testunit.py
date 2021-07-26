from application import app, db
from application.models import Farmers, Goods
from flask import url_for
from flask_testing import TestCase


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY="TEST_SECRET_KEY",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )

        return app

    
    def setUp(self):
                db.drop_all()
        db.create_all()
        farmer = Farmers(
            name='Test',
            farm='TestFarm',
            age='25',
        )

        db.session.add(farmer)
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
        equipment = "Spade",
        equipmenttype = "",
        vegetables = "Chillies",
        vegenum = 123,
        fruits = "Durian",
        fruitnum = 64,
        farmers_id = 1,
        )
        db.session.add(good)
        db.session.add(good2)
        db.session.commit()
    def tearDown(self):

        db.session.remove()
        db.drop_all()
class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)
        
    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)
class TestRead(TestBase):

    def test_read(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'Test', response.data)
        self.assertIn(b'TestFarm', response.data)
        self.assertIn(b'25', response.data)
        self.assertIn(b'Tractor', response.data)
class TestUpdate(TestBase):

    def test_update(self):
        response = self.client.post(
            url_for('update', id=1),
            follow_redirects= True,
            data = dict(
                name="Jules"
                
            )
        )

        self.assertIn(b'Jules',response.data)
class TestDelete(TestBase):

    def test_delete(self):
             
        response = self.client.get(
        url_for('delete', id=1),
        follow_redirects=True
        )

        assert "Test" not in response.data.decode()
