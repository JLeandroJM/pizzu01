from app import db
from datetime import datetime





class Local(db.Model):

    adress = db.Column(db.String(120), primary_key=True)
    reference = db.Column(db.String(64), index=True, unique=True)
    open = db.Column(db.Integer(),nullable= False)
    close = db.Column(db.Integer(),nullable= False)



class Bebidas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(),nullable = False)
    image = db.Column(db.String(300), nullable = False, unique = True)

class Pastas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(),nullable = False)
    image = db.Column(db.String(300), nullable = False, unique = True)




class User(db.Model):

    email = db.Column(db.String(120), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128),nullable=False)
    phone = db.Column(db.String(9),nullable =False, unique =True)
    adress =db.Column(db.String(200),nullable=False, unique = True)
    pedidos = db.relationship('Pedidos', backref='user', lazy='dynamic')


class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    product = db.Column(db.String(30), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    amount = db.Column(db.Float(),nullable = False)
    user_email = db.Column(db.String(120), db.ForeignKey('user.email'),nullable = False)
    
    


association_table = db.Table('Relation',
db.Column('pizza_id', db.Integer, db.ForeignKey('pizzas.id'), primary_key=True),
db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)
)


class Pizzas(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    size = db.Column(db.String(15),nullable = False)
    price = db.Column(db.Float(),nullable = False)
    image = db.Column(db.String(300), nullable = False, unique = True)


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(),nullable = False)
    image = db.Column(db.String(300), nullable = False, unique = True)

