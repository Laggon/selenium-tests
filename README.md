# Браузерные тесты на Selenium

Сущности:

* Файлы с префиксом `test_**.py` - тесты
* Файлы в папке `pages` - страницы в соответствии с их адресом, используются в тестах
* Файлы в папке `components` - компоненты используемые в страницах

## Установка

```sh
python -m venv .venv
```

```sh
source .venv/bin/activate
```

```sh
pip install -r requirements.txt
```

```sh
cp .env.example .env
```

## Запуск

```sh
pytest -s
```
