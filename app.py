from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename="404.jpg")
    return'''
<!doctype html>
<html>
    <head>
        <style>
            body {
                font-family: Algerian;
                background-color: bisque;
                text-align: center;
            }

            h1 {
                color: red;
            }
            img {
                 width: 1200px; 
                height: auto; 
            }

        </style>
    </head>
    <body>
        <h1>Упс... Такой страницы не найдено :(</h1>
        <img src="''' + path + '''">
    </body>
</html>
''', 404


@app.route("/")
@app.route("/index")
def index():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        <ol>
            <li><a href="/lab1">Первая лабораторная</a></li>
        </ol>
        <footer>
            Посаженников Сергей Александровчи, ФБИ-22, 3 Курс, 2024 год
        </footer>
    </body>
</html>
'''
@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
    </head>
    <body>
        <h1>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </h1>
        <a href="/">Корень сайта:</a>
    </body>
'''

@app.route("/")
@app.route("/lab1/web")
def web():
    return """<!doctype html> 
        <html>
           <body> 
               <h1>web-сервер на flask</h1>
               <a href="/author">author</a>
           </body> 
        </html>""",200, {
            'X-server': 'sample',
            'Content-Type': 'text/plan; charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Посаженников Сергей Александрович"
    group = "ФБИ-22"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>"""

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    css_url = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
        <br>
        <a href="/lab1/clear_counter">Очистить счетчик</a>
    </body>
</html>
'''

@app.route('/lab1/clear_counter')
def clear_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        Список очищен
        <br>
        <a href="/lab1/counter">Вернуться к счетчику</a>
        </br>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201

@app.route("/lab1/bad_request")
def bad_request():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Неправильный, некорректный запрос</h1>
    </body>
</html>
''', 400

@app.route("/lab1/unauthorized")
def unauthorized():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Авторизация не выполнена</h1>
    </body>
</html>
''', 401

@app.route("/lab1/payment_required")
def payment_required():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Необходима оплата</h1>
    </body>
</html>
''', 402

@app.route("/lab1/forbidden")
def forbidden():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Доступ запрещен</h1>
    </body>
</html>
''', 403

@app.route("/lab1/method_not_allowed")
def method_not_allowed():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Метод не поддерживается</h1>
    </body>
</html>
''', 405

@app.route("/lab1/teapot")
def teapot():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Сервер отказывается варить кофе, потому что это чайник ;)</h1>
    </body>
</html>
''', 418