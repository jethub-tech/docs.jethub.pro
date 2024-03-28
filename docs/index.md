# Главная

_TODO: добавить диаграмму_

## **Интеграция**
----

### **`API_PATH`**

Выдается отдельно для авторизации.

### **`CLIENT_TOKEN`**

Выдается отдельно для авторизации.

Стоит отметить, что токен указывается внутри кода (ниже пример), но ничего не мешает вынести как аргументом в командную строку.

### **Приложение** (на python3)

- Установка нужных зависимостей

    _TODO: дописать названия библиотек и их версии_
    ``` bash
    pip install click==8.1.7 requests==2.31.0
    ```

- Программа

    Для быстрого доступа к системе предлагается использоват следующий python код.

    ??? quote "`jethub_client_app.py`"

        _TODO: добавить код с обновленными doc-string_
        ```python linenums="1"
        --8<-- "docs/assets/example_jethub_client_app.py"
        ```

- Аргументы

    - `-p` – путь к файлу или папке
    - `-o` – путь выходного отчёта (по-умолчанию `jethub_report.json`)

    ``` bash
    python3 jethub_client_app.py -p ./src/core -o my_name_report .json
    ```

    ``` bash
    python3 jethub_client_app.py -p ./code2analize.py
    ```

## **Пример отчёта**
----

``` json linenums="1" title="jethub_report.json"
{
    "errors": [
        {
            "filename": "example_dir/Makefile.py",
            "reason": "syntax error while parsing AST from file"
        }
    ],
    "generated_at": "2024-03-03T17:36:52Z",
    "results": [
        {

        },
        {

        }
    ]
}
```
