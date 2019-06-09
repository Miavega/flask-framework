from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from app import app
from src.db.config import db
from src.models.usuario import Usuario

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    nombre = request.args.get('nombre')
    email = request.args.get('email')
    equipo = request.args.get('equipo')
    try:
        usuario = Usuario(
            nombre=nombre,
            email=email,
            equipo=equipo
        )
        db.session.add(usuario)
        db.session.commit()
        flash("Usuario creado. usuario id={}".format(usuario.id))
        return redirect(url_for('equipo'))
    except Exception as e:
        return(str(e))

@app.route('/modificar_usuario')
def modificar_usuario():
    return 'asdsa'

@app.route('/borrar_usuario')
def borrar_usuario():
    return 'asdsa'

@app.route('/consultar_usuario')
def consultar_usuario():
    return 'asdsa'
