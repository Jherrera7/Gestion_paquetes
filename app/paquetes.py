from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import true

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/gestionpaquetesutb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

#Creación de Tabla Categoria
class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(50))
    cat_prod = db.Column(db.String(20))

    def __init__(self,cat_now,cat_prod):
        self.cat_nom = cat_now
        self.cat_prod = cat_prod

db.create_all()

#Esquema Categoria
class CategoriaSchema(ma.Schema):
    class Login:
        fielts = ('cat_id','cat_nom','cat_prod')

#Una sola respusta
categoria_schema = CategoriaSchema()
#Cuando sean muchas respuestas
categorias_schema = CategoriaSchema (many=true)

#GET
@app.route('/categoria',methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categoria_schema.dump(all_categorias)
    return jsonify(result)

#Mensaje de Bienvenida 
@app.route('/',methods=['GET'])
def index():
    return jsonify({'Mensaje':'Bienvenido somos MensajeriaExpress UTB'})

if __name__=="__main__":
    app.run(debug=True) 