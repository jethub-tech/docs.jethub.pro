---
hide:
  - navigation
  - toc
---

# Главная

```mermaid
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart LR
    subgraph CLIENT [Пользователь]
        style CLIENT color:#fff
        direction RL

        subgraph JETHUB_client_app[jethub_client_app.py]
            style JETHUB_client_app color:#fff

            client_token([CLIENT_TOKEN])
            style client_token color:#fff

            JETHUB_api([API_PATH])
            style JETHUB_api color:#fff
        end

        path([файл или папка])
        style path color:#fff

        path --> JETHUB_client_app

    end

    subgraph JETHUB [JetHub]
        style JETHUB color:#fff
        direction LR

        identification([идентификация пользователя])
        style identification color:#fff

        subgraph JETHUB_tools[Инструменты]
            style JETHUB_tools color:#fff
            direction LR

            analizator([статический анализатор])
            style analizator color:#fff

            data_leaks([утечка данных])
            style data_leaks color:#fff

        end

        post_processing([постобработка])
        style post_processing color:#fff

        report([jethub_report.json])
        style report color:#fff

        identification -.-> JETHUB_tools

        JETHUB_tools -.-> post_processing
        post_processing -.-> report

    end

    CLIENT <--> JETHUB
```

## **Интеграция**
----

### **`API_PATH`**

Точка доступа предоставляется отдельно.

> Точка доступа указывается в клиентском приложении `jethub_client_app.py` как переменная `API_PATH`.

### **`CLIENT_TOKEN`**

Уникальный токен клиента предоставляется отдельно.

> Токен указывается в клиентском приложении `jethub_client_app.py` как переменная `CLIENT_TOKEN`.

### **Приложение** (на python3)

- Установка нужных зависимостей

    ```bash
    pip install click==8.1.7 requests==2.31.0
    ```

- Программа

    Для быстрого доступа к системе предлагается использоват следующий python код.

    ??? quote "`jethub_client_app.py`"

        ```python linenums="1"
        --8<-- "./docs/assets/example_jethub_client_app.py"
        ```

- Аргументы

    | Имя Полное   | Имя краткое | Описание                     | По-умолчанию         |
    | ------------ | ----------- | ---------------------------- | -------------------- |
    | `--path`     | `-p`        | Путь к файлу или папке       |  –                   |
    | `--out_file` | `-o`        | Путь выходного отчёта        | `jethub_report.json` |

    **Пример**

    ```bash
    python3 jethub_client_app.py -p my_python_code.py
    ```

## **`jethub_report.json`**
----

Весь перечень ошибок (в настоящий момент доступен только для языка python) можно посмотреть во [вкладке «Python»](https://docs.jethub.pro/python/).

### Пример отчёта

```json linenums="1" title="jethub_report.json"
{
    "code": 200,
    "msg": "Success response",
    "data": {
        "sast_python": [
            {
                "id": "JP0847B",
                "test_name": "blacklist",
                "path": "src/main.py",
                "code": "1 import pandas as pd\n2 from fastapi import *\n3",
                "line": 2,
                "line_range": [
                    2
                ],
                "col_offset": 0,
                "end_col_offset": 21,
                "severity": "HIGH",
                "confidence": "HIGH",
                "cwe_id": 1061,
                "cwe_link": "https://cwe.mitre.org/data/definitions/1061.html",
                "link_to_doc": "https://docs.jethub.pro/python/special/import/JP0847B-import_all"
            },
            {
                "id": "JP1225C",
                "test_name": "start_process_with_no_shell",
                "path": "src/utils.py",
                "code": "9 \n10 os.execl(path, arg0, arg1)\n",
                "line": 10,
                "line_range": [
                    10
                ],  
                "col_offset": 0,
                "end_col_offset": 26,
                "severity": "LOW",  
                "confidence": "MEDIUM",
                "cwe_id": 78,
                "cwe_link": "https://cwe.mitre.org/data/definitions/78.html",
                "link_to_doc": "https://docs.jethub.pro/python/common_errors/calls/injections/JP1225C-создание_процесса_через_os_без_shell"
            }
        ],
        "data_leaks": [
            {
                "path": "src/structure.py",
                "line": 10,
                "code": "AKIAQYLPMN5HHHFPZAM2"
            },
            {
                "path": "src/code/main.go",
                "line": 4,
                "code": "***the-internet.herokuapp.com"
            }
        ]
    }
}
```
