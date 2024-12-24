function fillFilmList() {
    fetch('/lab7/rest-api/films')
        .then(response => response.json())
        .then(films => {
            let tbody = document.getElementById('film-list');
            tbody.innerHTML = '';
            films.forEach((film, i) => {
                let tr = document.createElement('tr');
                let tdTitle = document.createElement('td');
                let tdTitleRus = document.createElement('td');
                let tdYear = document.createElement('td');
                let tdActions = document.createElement('td');

                tdTitle.innerText = film.title === film.title_ru ? '' : film.title;
                tdTitleRus.innerText = film.title_ru;
                tdYear.innerText = film.year;

                let editButton = document.createElement('button');
                editButton.innerText = 'редактировать';
                editButton.onclick = () => editFilm(i);

                let delButton = document.createElement('button');
                delButton.innerText = 'удалить';
                delButton.onclick = () => deleteFilm(i, film.title_ru);

                tdActions.append(editButton, delButton);
                tr.append(tdTitle, tdTitleRus, tdYear, tdActions);
                tbody.append(tr);
            });
        });
}

function deleteFilm(id, title) {
    if (!confirm(`Вы точно хотите удалить фильм "${title}"?`)) return;
    fetch(`/lab7/rest-api/films/${id}`, { method: 'DELETE' })
        .then(() => fillFilmList());
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
    document.getElementById('description-error').innerText = ''; 
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}

function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal();
}

function sendFilm() {
    const id = document.getElementById('id').value;
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: document.getElementById('year').value,
        description: document.getElementById('description').value
    };

    const url = `/lab7/rest-api/films/${id}`;
    const method = id === '' ? 'POST' : 'PUT';

    fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(film)
    })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw new Error(err.error) });
            }
            return response.json();
        })
        .then(() => {
            fillFilmList();
            hideModal();
        })
        .catch(error => {
            document.getElementById('description-error').innerText = error.message;
        });
}

function editFilm(id) {
    fetch(`/lab7/rest-api/films/${id}`)
        .then(response => response.json())
        .then(film => {
            document.getElementById('id').value = id;
            document.getElementById('title').value = film.title;
            document.getElementById('title-ru').value = film.title_ru;
            document.getElementById('year').value = film.year;
            document.getElementById('description').value = film.description;
            showModal();
        });
}

document.addEventListener('DOMContentLoaded', () => {
    fillFilmList();
});