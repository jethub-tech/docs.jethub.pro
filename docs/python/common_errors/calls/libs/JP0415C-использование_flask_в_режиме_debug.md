# JP0415C
## Использование Flask в режиме debug

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

Flask в режиме отладки использует дебаггер Werkzeug, который открывает возможность исполнения произвольного кода. Данный режим не должен использоваться вне тестовой среды.

## Пример небезопасного использования

```python linenums="1"
from flask import Flask

app = Flask(__name__)
app.run(debug=True)
```

```bash
python -m flask run --host=0.0.0.0
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/80.html>
* <https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode>
