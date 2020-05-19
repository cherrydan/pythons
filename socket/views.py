""""
Функции для отображения вьюх в нашем
веб-"фреймворке"
"""


def index():
    """
    Выводим шаблон по корневому урлу
    """
    with open('templates/index.html') as template:
        return template.read()


def blog():
    """
    Выводим шаблон по урлу blog
    """
    with open('templates/blog.html') as template:
        return template.read()
