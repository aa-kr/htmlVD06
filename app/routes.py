from flask import render_template, request, redirect, url_for
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Отображаем введенные данные
        return render_template('blog.html', name=name, city=city, hobby=hobby, age=age)

    return render_template('blog.html')