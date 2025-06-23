from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Configuración de SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contraseña = db.Column(db.String(128), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/registro', methods=['POST'])
def registro():
    datos = request.json
    usuario = datos['usuario']
    contraseña = datos['contraseña']

    if Usuario.query.filter_by(usuario=usuario).first():
        return jsonify({"mensaje": "Usuario ya existe"}), 400

    contraseña_hash = bcrypt.generate_password_hash(contraseña).decode('utf-8')
    nuevo_usuario = Usuario(usuario=usuario, contraseña=contraseña_hash)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario registrado exitosamente"})

@app.route('/login', methods=['POST'])
def login():
    datos = request.json
    usuario = datos['usuario']
    contraseña = datos['contraseña']

    usuario_db = Usuario.query.filter_by(usuario=usuario).first()

    if usuario_db and bcrypt.check_password_hash(usuario_db.contraseña, contraseña):
        return jsonify({"mensaje": f"Bienvenido {usuario}"})
    else:
        return jsonify({"mensaje": "Credenciales incorrectas"}), 401


@app.route('/tareas', methods=['GET'])
def tareas():
    return "<h1>Bienvenido/a al sistema de tareas</h1>"


if __name__ == '__main__':
    app.run(debug=True)


