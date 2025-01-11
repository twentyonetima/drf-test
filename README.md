# TASK API DJANGO REST FRAMEWORK

## УСТАНОВКА

### 1. Клонирование репозитория:

```bash
git clone https://github.com/twentyonetima/drf-test.git
```

### 2. Создание виртуальной среды:

```bash
python -m venv venv
```

### 3. Активация виртуальной среды и установка зависимостей:

```bash
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

```bash
pip install rq.txt
```

### 4. Выполнение миграций и старт сервера:

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

## Примеры запросов

### POST

```bash
curl -X POST http://127.0.0.1:8000/tasks/ -H "Content-Type: application/json" -d '{"title": "TEST 1", "completed": false}'  #On PowerShell: Invoke-WebRequest -Uri http://127.0.0.1:8000/tasks/ -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"title": "TEST 1", "completed": false}'
```

Пример ответа:
```bash
{
    "id": 1,
    "title": "TEST 1",
    "is_completed": false
}
```



### GET

```bash
curl http://127.0.0.1:8000/tasks/
```

Пример ответа:
```bash
[
    {
        "id": 1,
        "title": "TEST 1",
        "is_completed": false
    },
    {
        "id": 2,
        "title": "TEST 2",
        "is_completed": false
    }
]
```

