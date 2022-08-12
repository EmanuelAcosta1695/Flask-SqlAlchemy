from utils.db import db

#ESTA ES LA TABLA!!
#desde db, q importe, traigo Model
class User(db.Model):
    #en cada uno hay q definir el tipo de dato
    #CAMBIAR userId
    userid = db.Column(db.Integer, primary_key=True) #metodo column -> para definir columnas
    username = db.Column(db.String(100)) #tipo, caract unico. () -> longitud
    email = db.Column(db.String(100)) 
    password = db.Column(db.String(250)) 

    #utilizo el constructor para definir sus datos
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

#__tablename__ = "user"