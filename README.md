# Stripe payment + Djando

###  Задачи проекта: дать возможность пользователю выбрать товар из БД и имитировать оплату при помощи Stripe.  

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
