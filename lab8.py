from flask import Flask, Blueprint, render_template, request, jsonify, session

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/lab8.html')
