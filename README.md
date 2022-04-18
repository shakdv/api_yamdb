
# Проект «API для YaMDb»

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles).
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий (Category) может быть расширен администратором (например, 
можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. 
Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники»,
 а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например,
 «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review)
и ставят произведению оценку в диапазоне от одного до десяти (целое число);
из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число).
На одно произведение пользователь может оставить только один отзыв.

## Технологии
* Python 3.2
* Django 2.2
* DRF
* JWT
## Установка и запуск

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/shakdv/api_yamdb.git
```

```bash
cd api_yamdb
```

Создать и активировать виртуальное окружение:
```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

```bash
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python3 manage.py migrate --run-syncdb
```

Создаем суперпользователя:
```bash
python3 manage.py createsuperuser
```

Проект можно наполнить тестовыми данными:
```bash
python3 manage.py importcsv
```

Запустить проект:
```bash
python3 manage.py runserver
```

## Пользовательские роли
* Аноним — может просматривать описания произведений, читать отзывы и комментарии.
* Аутентифицированный пользователь (user) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
* Модератор (moderator) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
* Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
* Суперюзер Django должен всегда обладать правами администратора, пользователя с правами admin. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.

## Документация по API YaMDb
Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API YaMDb.
В документации описано, как работает API.
Документация представлена в формате Redoc.

## Регистрация нового пользователя
Получить код подтверждения на переданный email.
Права доступа: Доступно без токена.
Использовать имя 'me' в качестве username запрещено.
Поля email и username должны быть уникальными.

Регистрация нового пользователя:
```
POST /api/v1/auth/signup/

{
  "email": "string",
  "username": "string"
}
```

Получение JWT-токена:
```
POST /api/v1/auth/token/

{
  "username": "string",
  "confirmation_code": "string"
}
```

## Примеры работы с API для авторизованных пользователей
Добавление категории:
```
Права доступа: Администратор.
POST /api/v1/categories/

{
  "name": "string",
  "slug": "string"
}
```

Удаление категории:
```
Права доступа: Администратор.
DELETE /api/v1/categories/{slug}/
```

Добавление жанра:
```
Права доступа: Администратор.
POST /api/v1/genres/

{
  "name": "string",
  "slug": "string"
}
```

Удаление жанра:
```
Права доступа: Администратор.
DELETE /api/v1/genres/{slug}/
```

Обновление публикации:
```
PUT /api/v1/posts/{id}/

{
"text": "string",
"image": "string",
"group": 0
}
```

Добавление произведения:
```
Права доступа: Администратор. 
Нельзя добавлять произведения, которые еще не вышли (год выпуска не может быть больше текущего).
POST /api/v1/titles/

{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Получение произведения:
```
Права доступа: Доступно без токена
GET /api/v1/titles/{titles_id}/

{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```

Частичное обновление информации о произведении:
```
Права доступа: Администратор
PATCH /api/v1/titles/{titles_id}/

{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Частичное обновление информации о произведении:
```
Права доступа: Администратор
DEL /api/v1/titles/{titles_id}/
```

## Работа с пользователями
Получение списка всех пользователей:
```
Права доступа: Администратор
GET /api/v1/users/ - Получение списка всех пользователей
```

Добавление пользователя:
```
Права доступа: Администратор
Поля email и username должны быть уникальными.
POST /api/v1/users/ - Добавление пользователя

{
"username": "string",
"email": "user@example.com",
"first_name": "string",
"last_name": "string",
"bio": "string",
"role": "user"
}
```

Получение пользователя по username:
```
Права доступа: Администратор
GET /api/v1/users/{username}/ - Получение пользователя по username
```

Изменение данных пользователя по username:
```
Права доступа: Администратор
PATCH /api/v1/users/{username}/ - Изменение данных пользователя по username

{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

Удаление пользователя по username:
```
Права доступа: Администратор
DELETE /api/v1/users/{username}/ - Удаление пользователя по username
```

Получение данных своей учетной записи:
```
Права доступа: Любой авторизованный пользователь
GET /api/v1/users/me/ - Получение данных своей учетной записи
```

Изменение данных своей учетной записи:
```
Права доступа: Любой авторизованный пользователь
PATCH /api/v1/users/me/ - Изменение данных своей учетной записи
```
