---
hide:
  - navigation
  - toc
---

# Главная

``` mermaid
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

        analizator([статический анализатор])
        style analizator color:#fff

        post_processing([постобработка])
        style post_processing color:#fff

        report([jethub_report.json])
        style report color:#fff

        identification -.-> analizator
        analizator -.-> post_processing
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

    ``` bash
    pip install click==8.1.7 requests==2.31.0
    ```

- Программа

    Для быстрого доступа к системе предлагается использоват следующий python код.

    ??? quote "`jethub_client_app.py`"

        ```python linenums="1"
        --8<-- "./docs/assets/example_jethub_client_app.py"
        ```

- Аргументы

    - `-p` – путь к файлу или папке
    - `-o` – путь выходного отчёта (по-умолчанию `jethub_report.json`)

    ``` bash
    python3 jethub_client_app.py -p ./src/core -o my_name_report .json
    ```

    ``` bash
    python3 jethub_client_app.py -p ./my_python_code.py
    ```

## **`jethub_report.json`**
----

Весь перечень ошибок (в настоящий момент доступен только для языка python) можно посмотреть во [вкладке «Python»](https://docs.jethub.pro/python/).

### Пример отчёта

``` json linenums="1" title="jethub_report.json"
{
    "errors": [
        {
            "filename": "example_dir/Makefile.py",
            "reason": "syntax error while parsing AST from file"
        }
    ],
    "generated_at": "2024-03-08T18:36:52Z",
    "results": [
        {
            "code": "1 import pandas as pd\n2 from fastapi import *\n3",
            "col_offset": 0,
            "end_col_offset": 21,
            "filename": "example_src/example_main.py",
            "issue_confidence": "HIGH",
            "issue_severity": "HIGH",
            "line_number": 2,
            "line_range": [
                2
            ],
            "problem_cwe_id": 1061,
            "problem_cwe_link": "https://cwe.mitre.org/data/definitions/1061.html",
            "problem_id": "JP0847B",
            "test_name": "blacklist",
            "link_to_doc": "https://docs.jethub.pro/python/special/import/JP0847B-import_all"
        },
        {
            "code": "9 \n10 os.execl(path, arg0, arg1)\n",
            "col_offset": 0,
            "end_col_offset": 26,
            "filename": "example_src/example_utils.py",
            "issue_confidence": "MEDIUM",
            "issue_severity": "LOW",
            "line_number": 10,
            "line_range": [
                10
            ],
            "problem_cwe_id": 78,
            "problem_cwe_link": "https://cwe.mitre.org/data/definitions/78.html",
            "problem_id": "JP1225C",
            "test_name": "start_process_with_no_shell",
            "link_to_doc": "https://docs.jethub.pro/python/common_errors/calls/injections/JP1225C-создание_процесса_через_os_без_shell"
        }
    ]
}
```
