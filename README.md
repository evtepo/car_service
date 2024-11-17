# Car Service
Сервис предоставляет управление автомобилями и комментариями к ним.

## Запуск проекта
### Локально (Иметь установленный PostgreSQL, либо запущенный в Docker)
1. Создать .env файл и вставить значения из ```./src/configs/.env.example```.
2. Перейти в директорию с приложением:
   ```sh
   cd ./src
3. Выполнить команду:
   ```sh
   python ./manage.py runserver
### Docker
1. Перейти в директорию с приложением:
   ```sh
   cd ./src
2. Собрать статические файлы:
   ```sh
   python ./manage.py collectstatic --no-input
4. Перейти в корень проекта и выполнить команду:
   ```sh
   docker compose up --build

## Описание работы API
### Car
#### 1. Создание автомобиля
- **Метод**: `POST`
- **URL**: `http://localhost:80/api/v1/car/`
- **Тело запроса** (JSON):
  ```json
  {
    "make": "TOYOTA",
    "model": "Camry",
    "year":  2021,
    "description": "Компактный седан с отличной экономией топливаи современными технологиями безопасности."
  }
  ```
#### 2. Получение списка автомобилей и комментариев
- **Метод**: `GET`
- **URL**: `http://localhost:80/api/v1/car/`
#### 3. Обновление автомобиля
- **Метод**: `PUT`
- **URL**: `http://localhost:80/api/v1/car/<car_id>/`
- **Тело запроса** (JSON):
  ```json
  {
    "make": "TOYOTA",
    "model": "Camry",
    "year":  2020,
    "description": "Обновленное описание."
  }
  ```
#### 4. Удаление автомобиля
- **Метод**: `DELETE`
- **URL**: `http://localhost:80/api/v1/car/<car_id>/`
### Comment
#### 1. Создание комментария
- **Метод**: `POST`
- **URL**: `http://localhost:80/api/v1/comment/<car_id>/`
- **Тело запроса** (JSON):
  ```json
  {
    "content": "Комментарий для Camry"
  }
  ```
#### 2. Получение комментариев
- **Метод**: `GET`
- **URL**: `http://localhost:80/api/v1/comment/<car_id>/`

## Используемые технологии
| Компонент                       | Технология                                    |
|---------------------------------|-----------------------------------------------|
| **Фреймворк для Car Service**   | [Django](https://www.djangoproject.com/)      |
| **Фреймворк для Car API**       | [DRF](https://www.django-rest-framework.org/) |
| **Веб-сервер**                  | [Nginx](https://www.nginx.com/)               |
| **База данных**                 | [PostgreSQL](https://www.postgresql.org/)     |
| **Контейнеризация**             | [Docker](https://www.docker.com/)             |
