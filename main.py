# Активация виртуалки ll_env\scripts\activate.bat
# Команда создания django проекта django-admin имя_проекта .
# Файл settings.py определяет то, как Django взаимодействует с вашей системой и управляет вашим проектом.
# Файл urls.py сообщает Django, какие страницы следует строить в ответ на запросы браузера.
# Файл wsgi.py помогает Django предоставлять созданные файлы (имя файла является сокращением от «Web Server Gateway Interface»)
# Каждое изменение базы данных называется миграцией.
# Первое выполнение команды migrate приказывает Django проверить, что база данных соответствует текущему состоянию проекта.
# python manage.py runserver - запуск сервера django
# Команда startapp имя_приложения приказывает Django создать инфраструктуру,необходимую для построения приложения.


# Модель сообщает Django, как работать с данными, которые будут храниться в приложении.
# С точки зрения кода модель представляет собой обычный класс;
# она содержит атрибуты и методы, как и все остальные классы

# python manage.py makemigrations - По команде makemigrations Django определяет, как изменить базу данных для хранения информации, связанной с новыми моделями.
# python manage.py migrate - выполнение миграции

#  имя_модели.objects.all() - получает все экземпляры данной модели в режиме shell
#  имя_экземпляра_модели.имя_связанного_внешним_ключом_класса_set.all() - возвращает все экземпляры связанного внешнего ключом класса с текущим объектом