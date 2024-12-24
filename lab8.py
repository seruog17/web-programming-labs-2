from flask import Flask, Blueprint, redirect, render_template, request, jsonify, session
from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from db.models import users, articles
from flask_login import login_user, login_required, logout_user, current_user


lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    login = current_user.login if current_user.is_authenticated else None
    return render_template('lab8/lab8.html', login=login)

@lab8.route('/lab8/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if not login_form:
        return render_template('lab8/register.html', error='Имя пользователя не может быть пустым')
    
    if not password_form:
        return render_template('lab8/register.html', error='Пароль не может быть пустым')

    login_exists = users.query.filter_by(login=login_form).first()
    if login_exists:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')
    
    password_hash = generate_password_hash(password_form)
    new_user = users(login=login_form, password=password_hash)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=False)

    return redirect('/lab8/')

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')
    remember_me = request.form.get('remember_me')  

    if not login_form:
        return render_template('lab8/login.html', error='Логин не может быть пустым')
    
    if not password_form:
        return render_template('lab8/login.html', error='Пароль не может быть пустым')

    user = users.query.filter_by(login=login_form).first()
    if user:
        if check_password_hash(user.password, password_form):
            login_user(user, remember=remember_me == 'True')
            return redirect('/lab8/')
        
    return render_template('lab8/login.html', error='Ошибка входа: логин и/или пароль неверны')
    
@lab8.route('/lab8/articles')
@login_required
def article_list():
    user_articles = articles.query.filter_by(login_id=current_user.id).all()
    return render_template('lab8/articles.html', articles=user_articles)

@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'GET':
        return render_template('lab8/create_article.html')
    
    title = request.form.get('title')
    content = request.form.get('content')

    if not title:
        return render_template('lab8/create_article.html', error='Заголовок не может быть пустым')
    
    if not content:
        return render_template('lab8/create_article.html', error='Содержимое статьи не может быть пустым')

    new_article = articles(
        title=title,
        articles_text=content,
        login_id=current_user.id,
        is_favorite=False,
        is_public=True,
        likes=0
    )
    db.session.add(new_article)
    db.session.commit()

    return redirect('/lab8/')

@lab8.route('/lab8/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = articles.query.get(article_id)

    if not article or article.login_id != current_user.id:
        return render_template('lab8/articles.html', error='Статья не найдена')

    if request.method == 'GET':
        return render_template('lab8/edit_article.html', article=article)
    
    title = request.form.get('title')
    content = request.form.get('content')

    if not title:
        return render_template('lab8/edit_article.html', article=article, error='Заголовок не может быть пустым')
    
    if not content:
        return render_template('lab8/edit_article.html', article=article, error='Содержимое статьи не может быть пустым')

    article.title = title
    article.articles_text = content
    db.session.commit()

    return redirect('/lab8/articles')

@lab8.route('/lab8/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    article = articles.query.get(article_id)

    if not article or article.login_id != current_user.id:
        return render_template('lab8/articles.html', error='Статья не найдена')

    db.session.delete(article)
    db.session.commit()

    return redirect('/lab8/articles')