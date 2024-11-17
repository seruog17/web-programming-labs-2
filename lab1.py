from flask import Blueprint, url_for, redirect
lab1 = Blueprint('lab1', __name__)


@lab1.route("/lab1/")
def lab():
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

        <h2>Список роутов</h2>
        <ul>
            <li><a href="/lab1/web">web</a></li>
            <li><a href="/lab1/author">author</a></li>
            <li><a href="/lab1/oak">oak</a></li>
            <li><a href="/lab1/counter">counter</a></li>
            <li><a href="/lab1/clear_counter">clear_counter</a></li>
            <li><a href="/lab1/info">info</a></li>
            <li><a href="/lab1/created">created</a></li>
            <li><a href="/lab1/bad_request">bad_request</a></li>
            <li><a href="/lab1/unauthorized">unauthorized</a></li>
            <li><a href="/lab1/payment_required">payment_required</a></li>
            <li><a href="/lab1/forbidden">forbidden</a></li>
            <li><a href="/lab1/method_not_allowed">method_not_allowed</a></li>
            <li><a href="/lab1/teapot">teapot</a></li>
            <li><a href="/lab1/null">null</a></li>
        </ul>
    </body>
'''


@lab1.route("/lab1/web")
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


@lab1.route("/lab1/author")
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


@lab1.route('/lab1/oak')
def oak():
    path = url_for("static", filename="lab1/oak.jpg")
    css_url = url_for("static", filename="lab1/lab1.css")
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


@lab1.route('/lab1/counter')
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


@lab1.route('/lab1/clear_counter')
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


@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")


@lab1.route("/lab1/created")
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


@lab1.route("/lab1/bad_request")
def bad_request():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Неправильный, некорректный запрос</h1>
    </body>
</html>
''', 400


@lab1.route("/lab1/unauthorized")
def unauthorized():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Авторизация не выполнена</h1>
    </body>
</html>
''', 401


@lab1.route("/lab1/payment_required")
def payment_required():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Необходима оплата</h1>
    </body>
</html>
''', 402


@lab1.route("/lab1/forbidden")
def forbidden():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Доступ запрещен</h1>
    </body>
</html>
''', 403


@lab1.route("/lab1/method_not_allowed")
def method_not_allowed():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Метод не поддерживается</h1>
    </body>
</html>
''', 405


@lab1.route("/lab1/teapot")
def teapot():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Сервер отказывается варить кофе, потому что это чайник ;)</h1>
    </body>
</html>
''', 418


@lab1.route("/lab1/null")
def null():
    result = 1 / 0
    return str(result)

