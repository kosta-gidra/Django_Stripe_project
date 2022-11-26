# Stripe payment + Djando

###  Задачи проекта: Реализовать сервер на Django, который общается со Stripe и создает платежные формы для товаров.  

**stripe** – платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей. С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции.

### Документация по проекту

В проекте используются переменные окружения. Необходимо создать файл .env с полями:
```
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
STRIPE_PUB_KEY=
STRIPE_SEC_KEY=
```
### Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить команду:

```bash
python manage.py runserver
```

Позиции в заказе и сам заказ создается через Django Admin панель. 
Для просмотра и оплаты заказа нужно перейти на ссылку /order/id.