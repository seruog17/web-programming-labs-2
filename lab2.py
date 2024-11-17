from flask import Blueprint, url_for, redirect, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]

@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    if not name:
        abort(400, description="Вы не задали имя цветка")
    
    flower_list.append(name)
    return f'''
    <!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

@lab2.route('/lab2/example')
def example():
    name = 'Сергей Посаженников'
    lab_number = '2'
    group = 'ФБИ-22'
    course = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95} ,
        {'name': 'манго', 'price': 321}
        ]
    return render_template('lab2/example.html', 
                           name=name, lab_number=lab_number, group=group,
                             course=course, fruits=fruits)

@lab2.route('/lab2/')
def lab23():
    return render_template('lab2/lab2.html')

@lab2.route('/lab2/filters')
def filters():
    pharse = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', pharse=pharse)

@lab2.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('lab2.calc', a=1, b=1))

@lab2.route('/lab2/calc/<int:a>')
def calc_with_one_param(a):
    return redirect(url_for('lab2.calc', a=a, b=1))

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    div_result = a / b if b != 0 else "Деление на ноль!"
    pow_result = a ** b

    return render_template('lab2/calc.html', a=a, b=b, sum_result=sum_result, diff_result=diff_result, 
                           prod_result=prod_result, div_result=div_result, pow_result=pow_result)


books = [
    {"author": "Дж. Р. Р. Толкин", "title": "Хоббит", "genre": "Фэнтези", "pages": 310},
    {"author": "Агата Кристи", "title": "И никого не стало", "genre": "Детектив", "pages": 272},
    {"author": "Дж. К. Роулинг", "title": "Гарри Поттер и философский камень", "genre": "Фэнтези", "pages": 309},
    {"author": "Антуан де Сент-Экзюпери", "title": "Маленький принц", "genre": "Философская сказка", "pages": 96},
    {"author": "Дж. Р. Р. Толкин", "title": "Властелин колец", "genre": "Фэнтези", "pages": 1178},
    {"author": "Чарльз Диккенс", "title": "Повесть о двух городах", "genre": "Исторический роман", "pages": 341},
    {"author": "Мигель де Сервантес", "title": "Дон Кихот", "genre": "Роман", "pages": 1056},
    {"author": "Мао Цзэдун", "title": "Цитаты председателя Мао Цзэдуна", "genre": "Политическая литература", "pages": 448},
    {"author": "Роберт Грин", "title": "48 законов власти", "genre": "Саморазвитие", "pages": 496},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 480}
]

@lab2.route('/lab2/books')
def books_list():
    return render_template('lab2/books.html', books=books)

rolex_watches = [
    {
        "name": "Rolex Submariner",
        "description": "Классические водонепроницаемые часы с хронометром.",
        "image": "lab2/rol1.jpg"
    },
    {
        "name": "Rolex Day-Date",
        "description": "Элегантные часы с датой и днем недели.",
        "image": "lab2/rol2.jpg"
    },
    {
        "name": "Rolex GMT-Master II",
        "description": "Часы с двумя часовыми поясами для путешественников.",
        "image": "lab2/rol3.png"
    },
    {
        "name": "Rolex Datejust",
        "description": "Классические часы с датой и хронометром.",
        "image": "lab2/rol4.jpg"
    },
    {
        "name": "Rolex Sky-Dweller",
        "description": "Часы с сложным механизмом для путешественников.",
        "image": "lab2/rol5.jpg"
    }
]

@lab2.route('/lab2/rolex')
def rolex_list():
    return render_template('lab2/rolex.html', watches=rolex_watches)