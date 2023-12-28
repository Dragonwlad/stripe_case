# Описание проекта Stripe_case

Тестовое задание с применением Stripe API. 

Ссылки:
* http://stripetestcase.ddns.net/payment/1/order/  страница покупки по order двух позиций item
* http://stripetestcase.ddns.net/payment/1/item/   страница покупки выбранного item
* http://stripetestcase.ddns.net/admin/
* Логин: admin Пароль: admin

## Технологии
* Backand: Django REST API, Stripe, Docker, NGINX

## В состав проекта входят 2 контейнера:

* stripe_case_gateway - Nginx Web-сервер.
* stripe_case_ - Django-сервер.

## Автор:
[Владислав Кузнецов](https://github.com/Dragonwlad)