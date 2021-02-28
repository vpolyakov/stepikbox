# stepikbox
Django REST Framework API

**Установка**

Установите python 3.9, создайте виртуальное окружение. 

В этом окружении с помощью pip -r requirements.txt установите Django и Django REST framework и др. нужные пакеты

Выполните миграцию: python manage migrate

Создайте superuser: python manage createsuperuser и измениет его id в бд на 0.

Сделайте первоначально заполнение бд: python manage import_users, python manage import_items, python manage import_reviews

запустите локально сервер: python manage runserver
