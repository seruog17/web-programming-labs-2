from flask import Flask, Blueprint, render_template, request, jsonify, session  
 
lab7 = Blueprint('lab7', __name__)  

@lab7.route('/lab7/')  
def main():  
    return render_template('lab7/index.html')  


films = [
    {
        "titile": "Fight Club",
        "title_ru": "Бойцовский клуб",
        "year": "1999",
        "description": "Сотрудник страховой компании страдает \
        хронической бессонницей и отчаянно пытается вырваться \
        из мучительно скучной жизни. Однажды в очередной командировке \
        он встречает некоего Тайлера Дёрдена — харизматического \
        торговца мылом с извращенной философией. Тайлер уверен, \
        что самосовершенствование — удел слабых, а единственное, \
        ради чего стоит жить, — саморазрушение.\
        Проходит немного времени, и вот уже новые друзья\
        лупят друг друга почем зря на стоянке перед баром, \
        и очищающий мордобой доставляет им высшее блаженство. \
        Приобщая других мужчин к простым радостям физической жестокости, \
        они основывают тайный Бойцовский клуб,\
        который начинает пользоваться невероятной популярностью."
    },
    {
        "titile": "The Green Mile",
        "title_ru": "Зеленая миля",
        "year": "1999",
        "description": "Пол Эджкомб — начальник блока смертников \
        в тюрьме «Холодная гора», каждый \
        из узников которого однажды проходит \
        «зеленую милю» по пути к месту казни. \
        Пол повидал много заключённых и надзирателей \
        за время работы. Однако гигант Джон Коффи, \
        обвинённый в страшном преступлении, стал \
         одним из самых необычных обитателей блока." 
    },
    {
        "titile": "The Gentlemen",
        "title_ru": "Джентльмены",
        "year": "2019",
        "description": "Один ушлый американец ещё со студенческих \
        лет приторговывал наркотиками, а теперь придумал \
        схему нелегального обогащения с использованием \
        поместий обедневшей английской аристократии и \
        очень неплохо на этом разбогател. Другой пронырливый \
        журналист приходит к Рэю, правой руке американца, \
        и предлагает тому купить киносценарий, в котором \
        подробно описаны преступления его босса при участии \
        других представителей лондонского криминального мира — партнёра-еврея, \
        китайской диаспоры, чернокожих спортсменов и даже русского олигарха."
    },
    {
        "titile": "Pulp Fiction",
        "title_ru": "Криминальное чтиво",
        "year": "1994",
        "description": "Двое бандитов Винсент Вега и Джулс Винфилд \
        ведут философские беседы в перерывах между разборками \
        и решением проблем с должниками криминального босса \
        Марселласа Уоллеса.В первой истории Винсент проводит \
        незабываемый вечер с женой Марселласа Мией. \
        Во второй Марселлас покупает боксёра Бутча Кулиджа, \
        чтобы тот сдал бой. В третьей истории Винсент и \
        Джулс по нелепой случайности попадают в неприятности."
    },
    {
        "titile": "The Godfather",
        "title_ru": "Крестный отец",
        "year": "1972",
        "description": "Глава семьи, Дон Вито Корлеоне, \
        выдаёт замуж свою дочь. В это время со Второй \
        мировой войны возвращается его любимый сын Майкл. \
        Майкл, герой войны, гордость семьи, не выражает \
        желания заняться жестоким семейным бизнесом. \
        Дон Корлеоне ведёт дела по старым правилам, но \
        наступают иные времена, и появляются люди, \
        елающие изменить сложившиеся порядки. \
        На Дона Корлеоне совершается покушение."
    },

]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Film not found"}), 404
    return jsonify(films[id])

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Film not found"}), 404
    del films[id]
    return '', 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Film not found"}), 404
    film = request.get_json()
    films[id] = film
    return films[id]



@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_films():
    new_film = request.get_json()
    films.append(new_film)
    new_film_index = len(films) - 1
    return {"index": new_film_index}, 201

