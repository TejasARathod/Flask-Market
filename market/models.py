from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin # The class that you use to represent users needs to implement properties and methods for login

'''You will need to provide a user_loader callback. 
This callback is used to reload the user object from the user ID stored in the session. 
It should take the str ID of a user, and return the corresponding user object'''

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=100000)
    # here db is not a column but a relationship
    items = db.relationship('Item', backref='owned_user', lazy=True) # backreference to see the owner of the item; lazy is set up otherwise sqlalchemy will not grab all the objects in items in one shot

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'Rs.{str(self.budget)[:-3]},{str(self.budget)[-3:]}'
        else:
            return f"Rs.{self.budget}"

    @property
    def password(self):
        return self

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password) # returns either true or false

    def can_purchase(self, item_obg):
        return self.budget >= item_obg.price

    def can_sell(self, item_obj):
        return item_obj in self.items

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True) # convention for sql , its a must for flask model sp that it recognizes unique objects
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id')) # Foreign key searches for the primary key , this going to be related with id in User Class

    def __repr__(self):
        return f'Item {self.name}'

    def buy(self, user):
        self.owner =  user.id
        user.budget -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner =  None
        user.budget += self.price
        db.session.commit()

    