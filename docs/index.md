---
hide:
  - navigation
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

## **Приложение** (на python3)
----

- Установка зависимостей

    ```bash
    pip install click==8.1.7 requests==2.31.0
    ```

- Программа

    Для быстрого доступа к системе предлагается использовать следующий python код.

    ??? quote "`jethub_client_app.py`"

        ```python linenums="1"
        --8<-- "./docs/assets/example_jethub_client_app.py"
        ```

- `API_PATH` и `CLIENT_TOKEN` предоставляются отдельно

- Аргументы

    | Имя                          | Описание                                                      | Условие                    | Замечение                                                                               |
    | ---------------------------- | --------------------------------------------------------------| -------------------------- | --------------------------------------------------------------------------------------- |
    | `--path`                     | Путь файла или папки для анализа                              | -                          | -                                                                                       |
    | `--out_file`                 | Путь-имя выходного отчёта (по-умолчанию `jethub_report.json`) | -                          | -                                                                                       |
    | `--sast-python-skiptest`     | Список идентификаторов уязвимостей (`id`) для игнорирования   | Через запятую, без пробела | Только для САК-python. В строке уязвимости можно использовать `# nosec`                 |
    | `--sast-python-exclude-path` | Список файлов-папок (`path`) для игнорирования                | Через запятую, без пробела | Только для САК-python                                                                   |
    | `--data-leaks-exlude-path`   | Список файлов-папок (`path`) для игнорирования                | Через запятую, без пробела | Только для утечки данных. В строке утечки можно использовать `# nosec` или `// nosec`   |
    | `—-global-exlude-path`       | Глобальный список файлов-папок (`path`) для игнорирования     | Через запятую, без пробела | Для САК-python и утечки данных. Eсли `path` одинаковый для `sast_python` и `data_leaks` |

    **Пример**

    ```bash
    python3 jethub_client_app.py --path src/core/ --sast-python-skiptest JP0817B,JP1219C --data-leaks-exlude-path tests/test_func.py
    ```

## **`jethub_report.json`**
----

Перечень ошибок (в настоящий момент доступен только для python) можно посмотреть во [вкладке «Python»](https://docs.jethub.pro/python/).

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
