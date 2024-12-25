from flask import Flask, Blueprint, redirect, render_template, request, jsonify, session
from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from db.models import users, articles
from flask_login import login_user, login_required, logout_user, current_user


lab9 = Blueprint('lab9', __name__)

@lab8.route('/lab9/')
def main():
    return render_template('lab9/index.html')