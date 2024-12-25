from flask import Flask, Blueprint, redirect, render_template, request, jsonify, session
from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from db.models import users, articles
from flask_login import login_user, login_required, logout_user, current_user

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')

@lab9.route('/lab9/age', methods=['POST'])
def age():
    name = request.form.get('name')
    session['name'] = name 
    return render_template('lab9/age.html', name=name)

@lab9.route('/lab9/gender', methods=['POST'])
def gender():
    age = request.form.get('age')
    session['age'] = age  
    return render_template('lab9/gender.html', name=session.get('name'), age=age)

@lab9.route('/lab9/preference', methods=['POST'])
def preference():
    gender = request.form.get('gender')
    session['gender'] = gender
    return render_template('lab9/preference.html', name=session.get('name'), age=session.get('age'), gender=gender)

@lab9.route('/lab9/detail', methods=['POST'])
def detail():
    preference = request.form.get('preference')
    session['preference'] = preference  
    return render_template('lab9/detail.html', name=session.get('name'), age=session.get('age'), gender=session.get('gender'), preference=preference)

@lab9.route('/lab9/result', methods=['POST'])
def result():
    detail = request.form.get('detail')
    session['detail'] = detail 

    name = session.get('name')
    age = session.get('age')
    gender = session.get('gender')
    preference = session.get('preference')
    detail = session.get('detail')

    if preference == 'tasty':
        if detail == 'sweet':
            gift = 'мешочек конфет'
            image = 'candy.jpg'
        else:
            gift = 'сытный пирог'
            image = 'pie.jpg'
    else:
        if detail == 'flowers':
            gift = 'букет цветов'
            image = 'flowers.jpg'
        else:
            gift = 'красивый тортик'
            image = 'cake.jpg'

    return render_template('lab9/result.html', name=name, age=age, gender=gender, gift=gift, image=image)