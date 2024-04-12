# JP0415C
## Использование `flask` в режиме отладки

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

----
Конфигурация `Flask` приложения с использованием фиксированных значений не рекомендуется. Предпочтительнее применять параметры, которые зависят от текущего окружения, так как это позволяет защитить сервис от случайной активации, например, тестового режима или режима отладки в производственной среде.

Например, `Flask` в режиме отладки использует дебаггер Werkzeug, который открывает возможность исполнения произвольного кода. Данный режим не должен использоваться вне тестовой среды.

Проверка срабатывает при записи константных значений для параметров `DEBUG, TESTING, ENV, SECRET_KEY` в словарь `config` с использованием функции `config.update()`, а также при передаче константного значения в аргумент `debug` непосредственно при запуске приложения с использованием `app.run(debug=Value)`.

## Пример небезопасного использования

```python linenums="1"
from flask import Flask

app = Flask(__name__)
# use argument write of hardcoded value
app.run(debug=True)
app.run(debug=False)
app.config.update(DEBUG=True)
app.config.update(TESTING=True)
app.config.update(SECRET_KEY="aaaa")
# OK - no hardcoded value
app.config.update(TESTING=os.getenv("TESTING"))
```

```bash
python -m flask run --host=0.0.0.0
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/94.html>
* <https://flask.palletsprojects.com/en/3.0.x/config/>
* <https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode>
