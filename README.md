# Pet Store API Test

##  Что это такое
Это набор автоматизированных тестов на Python для API сервиса «Pet Store» — проверяются основные эндпоинты (работа с питомцами, пользователями и магазином). Проект использует фреймворк тестирования **pytest** и предназначен для верификации, что API возвращает ожидаемые данные / поведения.


##  Как запускать
1. Склонируй репозиторий:
```bash
git clone https://github.com/modongwan/pet_store_api_test.git
cd pet_store_api_test

```

Создай и активируй виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

Установи зависимости:
```bash
pip install pytest requests faker
```

Запусти все тесты:
```bash
pytest -v
```



