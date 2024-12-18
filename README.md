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
```hon3 manage.py runserver
```