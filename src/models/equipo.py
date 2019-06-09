from src.db.config import db


class Equipo(db.Model):
    __tablename__ = 'equipo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    desc_equipo = db.Column(db.String(80))

    def __init__(self, nombre, desc_equipo):
        self.nombre = nombre
        self.desc_equipo = desc_equipo

    def __repr__(self):
        return '<nombre {}>'.format(self.nombre)

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'desc_equipol': self.desc_equipo,
        }
