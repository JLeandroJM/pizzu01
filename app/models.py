from app import db

class User(db.Model):

    email = db.Column(db.String(120), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128),nullable=False)
    phone = db.Column(db.String(9),nullable =False)
    adress =db.Column(db.String(200),nullable=False)

class Locales(db.Model):

    adress = db.Column(db.String(120), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    opens = db.Column(db.Integer(),nullable= False)
    clases = db.Column(db.Integer(),nullable= False)

class Pizzas(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    size = db.Column(db.String(15),nullable = False)
    price = db.Column(db.Integer(),nullable = False)

class Bebidas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(),nullable = False)

class Pastas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(),nullable = False)

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    id_producto = db.Column(db.Integer(), db.ForeignKey('pizzas.id'), nullable=False)  
    pizzas = db.relationship("Pizzas", backref="ingredients") 

class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.String(50), db.ForeignKey('usuario.email'), nullable=False)
    product = db.Column(db.String(30), nullable=False)
    amount = db.Column(db.Integer(),nullable = False)
    usuario = db.relationship("Usuario", backref="pedidos")
    time = db.Column(db.String(30), nullable=False)

