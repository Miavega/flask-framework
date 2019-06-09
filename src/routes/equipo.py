from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from app import app
from src.db.config import db
from src.models.equipo import Equipo

@app.route('/equipo')
def equipo():
	consulta = Equipo.query.all()
	return render_template('equipo.html', equipos=consulta)

@app.route('/crear_equipo', methods=['POST'])
def crear_equipo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        desc_equipo = request.form['desc_equipo']
        try:
            equipo = Equipo(
                nombre=nombre,
                desc_equipo=desc_equipo,
            )
            db.session.add(equipo)
            db.session.commit()
            flash("Equipo creado. equipo id={}".format(equipo.id))
            return redirect(url_for('equipo'))
        except Exception as e:
            return(str(e))

@app.route('/modificar_equipo')
def modificar_equipo():
    return 'asdsa'

@app.route('/borrar_equipo/<string:id>')
def borrar_equipo(id):
	try:
		equipo = Equipo.query.filter_by(id=id).first()
		db.session.delete(equipo)
		db.session.commit()
		return redirect(url_for('equipo'))
	except Exception as e:
		return(str(e))

@app.route('/consultar_equipo', methods=['GET'])
def consultar_equipo():
    try:
        equipos = Equipo.query.all()
        return jsonify([equipo.serialize() for equipo in equipos])
    except Exception as e:
        return(str(e))

