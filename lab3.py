from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    name_color = request.cookies.get('name_color')

    if name is None:
        name = 'аноним'
    if age is None:
        age = 'неизвестный'

    return render_template('lab3/lab3.html', name=name, age=age, name_color=name_color)

@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'


    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    price = request.args.get('price', type=int)
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        color = request.form.get('color')
        background_color = request.form.get('background_color')
        font_size = request.form.get('font_size')
        font_weight = request.form.get('font_weight')

        resp = make_response(redirect('/lab3/settings'))

        if color:
            resp.set_cookie('color', color)
        if background_color:
            resp.set_cookie('background_color', background_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if font_weight:
            resp.set_cookie('font_weight', font_weight)

        return resp

    color = request.cookies.get('color')
    background_color = request.cookies.get('background_color')
    font_size = request.cookies.get('font_size')
    font_weight = request.cookies.get('font_weight')

    return render_template('lab3/settings.html',
                           color=color,
                           background_color=background_color,
                           font_size=font_size,
                           font_weight=font_weight)


@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    resp = make_response(redirect('/lab3'))
    resp.delete_cookie('color')
    resp.delete_cookie('background_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('font_weight')
    return resp


@lab3.route('/lab3/ticket')
def ticket_form():
    return render_template('lab3/ticket_form.html')


@lab3.route('/lab3/ticket_submit', methods=['POST'])
def ticket_submit():
    fio = request.form.get('fio')
    shelf = request.form.get('shelf')
    bedding = 'да' if request.form.get('bedding') else 'нет'
    baggage = 'да' if request.form.get('baggage') else 'нет'
    age = int(request.form.get('age'))
    departure = request.form.get('departure')
    destination = request.form.get('destination')
    date = request.form.get('date')
    insurance = 'да' if request.form.get('insurance') else 'нет'

    if not fio or not shelf or not age or not departure or not destination or not date:
        return "Все поля должны быть заполнены", 400

    if age < 1 or age > 120:
        return "Возраст должен быть от 1 до 120 лет", 400

    base_price = 700 if age < 18 else 1000
    if shelf in ['нижняя', 'нижняя боковая']:
        base_price += 100
    if bedding == 'да':
        base_price += 75
    if baggage == 'да':
        base_price += 250
    if insurance == 'да':
        base_price += 150

    return render_template('lab3/ticket.html', fio=fio, 
                           shelf=shelf, bedding=bedding, 
                           baggage=baggage, age=age, 
                           departure=departure, 
                           destination=destination,
                           date=date, 
                           insurance=insurance, 
                           price=base_price)
