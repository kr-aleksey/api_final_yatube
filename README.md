# Yatube
## Социальная сеть для блогеров


**Yatube** - это социальная сеть, учебный проект в рамках курса Yandex Practicum - Python разработчик. Проект предоставляет REST API для работы c сообществами, постами, комментариями и подписками пользователей. В проекте реализовано разграничение прав пользователей.  

Автор: Алексей Кравцун


### Технологии

```
- Python
- Django
- Django REST framework
```


### Запуск проекта
Клонируйте репозиторий и перейдите в созданную директорию в командной строке:
```
git clone https://github.com/kr-aleksey/api_final_yatube.git
```
```
cd api_final_yatube
```
Создайте и активируйте виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполните миграции:

```
python3 manage.py migrate
```

Запустите проект:

```
python3 manage.py runserver
```

### Примеры некоторых запросов

Получить все посты:
```
GET /api/v1/posts/
```
Получить пост:
```
GET /api/v1/posts/{id}/
```
Добавить новый пост:
```
POST /api/v1/posts/
Payload.
Content type: application/json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Получить все подписки пользователя сделавшего запрос:
```
GET /api/v1/follow/
```
