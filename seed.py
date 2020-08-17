from models import db, Pet

from app import app

db.drop_all()
db.create_all()

""" Sample pet data"""

roland = Pet(name="Roland", species="Dog", photo_url=" https://images.unsplash.com/photo-1530126483408-aa533e55bdb2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1301&q=80", age=8,
             notes='A very good boy', available=False)
humphery = Pet(name="Humphery", species="Dog", photo_url="https://images.unsplash.com/photo-1561037404-61cd46aa615b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80", age=8,
               notes='A very good boy', available=False)
tukker = Pet(name="Tukker", species="Dog", photo_url="https://images.unsplash.com/photo-1560525821-d5615ef80c69?ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80", age=3,
             notes='A very good boy', available=True)
future = Pet(name="Future", species="Cat", photo_url="https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80", age=8,
             notes='A very good Kitty', available=False)
noodle = Pet(name="Noodle", species="Cat", photo_url="https://images.unsplash.com/photo-1561948955-570b270e7c36?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=859&q=80", age=8,
             notes='A very good Kitty', available=False)

db.session.add_all([roland, humphery, tukker, future, noodle])
db.session.commit()
