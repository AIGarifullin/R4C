# R4C — Robots for consumers

## Небольшая предыстория.
Давным-давно, в далёкой-далёкой галактике, была компания производящая различных роботов.

Каждый робот(**Robot**) имел определенную модель выраженную двух-символьной
последовательностью (например R2). Одновременно с этим, модель имела различные
версии (например D2). Напоминает популярный телефон различных моделей (11, 12, 13...) и его версии
(X, XS, Pro...). Вне компании роботов чаще всего называли по серийному номеру, объединяя модель и версию (например R2-D2).

Также у компании были покупатели (**Customer**) которые периодически заказывали того или иного робота.

Когда роботов не было в наличии - заказы покупателей (**Order**) попадали в список ожидания.

---
## Что делает данный код?
Это заготовка для сервиса, который ведет учет произведенных роботов,а также
выполняет некие операции связанные с этим процессом.

Сервис нацелен на удовлетворение потребностей трёх категорий пользователей:
- Технические специалисты компании. Они будут присылать информацию
- Менеджмент компании. Они будут запрашивать информацию
- Клиенты. Им будут отправляться информация
___

## Как с этим работать?
- Создать для этого проекта репозиторий на GitHub
- Открыть данный проект в редакторе/среде разработки которую вы используете
- Ознакомиться с задачами в файле tasks.md
- Написать понятный и поддерживаемый код для каждой задачи 
- Сделать по 1 отдельному PR с решением для каждой задачи
- Прислать ссылку на своё решение
___

## Установка и запуск
💡 ВЕРСИЯ Python 3.10

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас Windows (в Git Bash)

    ```
    source env/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Создать суперпользователя:

```
python3 blogicum/manage.py createsuperuser
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов:

### Получение списка роботов, имеющихся в наличии (GET-запрос):

```
http://127.0.0.1:8000/api/v1/robots/
```

Пример ответа:
```json
[    
    {
        "id": 1,
        "serial": "R2-D2",
        "model": "R2",
        "version": "D2",
        "created": "2020-10-05T10:59:59Z"
    },
    {
        "id": 2,
        "serial": "13-XS",
        "model": "13",
        "version": "XS",
        "created": "2021-12-25T08:46:00Z"
    },
    {
        "id": 3,
        "serial": "X5-LT",
        "model": "X5",
        "version": "LT",
        "created": "2022-06-06T12:05:10Z"
    }
]
```

### Получение информации о роботе по ID (GET-запрос):

```
http://127.0.0.1:8000/api/v1/robots/1/
```

Пример ответа:
```json
{
    "id": 1,
    "serial": "R2-D2",
    "model": "R2",
    "version": "D2",
    "created": "2020-10-05T10:59:59Z"
}
```

### Создание робота (POST-запрос):

```
http://127.0.0.1:8000/api/v1/robots/
```

Пример запроса:
```json
{
    "model":"R2",
    "version":"D3",
    "created":"2024-12-10 10:10:00"
}
```

Пример ответа:
```json
{
    "message": "Robot is created",
    "robot_id": 4
}
```

### Создание Excel-файл со сводкой по суммарным показателям производства роботов за последнюю неделю (GET-запрос):

```
http://127.0.0.1:8000/api/v1/robot-report/
```

Пример ответа:
![Сохранение файла robot_report.xlsx.](media/photo.png)

### Получение списка заказов (GET-запрос):

```
http://127.0.0.1:8000/api/v1/orders/
```

Пример ответа:
```json
[    
    {
        "id": 1,
        "customer": 1,
        "robot_serial": "R2-D2"
    },
    {
        "id": 2,
        "customer": 1,
        "robot_serial": "13-XS"
    },
    {
        "id": 3,
        "customer": 2,
        "robot_serial": "X5-LT"
    }
]
```

### Получение информации о заказе по ID (GET-запрос):

```
http://127.0.0.1:8000/api/v1/orders/1/
```

Пример ответа:
```json
{
    "id": 1,
    "customer": 1,
    "robot_serial": "R2-D2"
}
```

### Создание заказа на покупку робота (POST-запрос). В случае отсутствия робота, отправляется письмо покупателю:

```
http://127.0.0.1:8000/api/v1/orders/
```

Пример запроса:
```json
{
    "customer": 1,
    "robot_serial":"R2_D8"
}
```

Пример ответа:
```json
{
    "message": "Order is created",
    "order_id": 4
}
```
Текст письма:
```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit
Subject: Information about the sale of the robot
From: sales_department@r4c.com
To: pytja@mail.ru
Date: Wed, 18 Dec 2024 08:50:50 -0000
Message-ID: <173451185091.25608.12689118765935231987@WIN-ERLK3EHQVCD>

Добрый день!
Недавно вы интересовались нашим роботом модели R2, версии D8.
Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста,
свяжитесь с нами
```
-------------------------------------------------------------------------------
