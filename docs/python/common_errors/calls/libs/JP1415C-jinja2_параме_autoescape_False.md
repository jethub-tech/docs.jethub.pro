# JP1415C
## JP1415C использование Jinja2 с параметром `autoescape=False`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-red?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-red?style=for-the-badge)

Использование фреймворка Jinja2 без параметра `autoescape=True` отключает безопасный ввод HTML шаблонов и открывает уязвимость к XSS атакам. Jinja2 рекомендуется использовать с параметром `autoescape=True` в явном виде.

## Пример небезопасного использования

```python linenums="1"
import jinja2

environment = jinja2.Environment(autoescape=False)
template = environment.from_string("Hello, {{ name }}!")
template.render(name="World")
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/94.html>
* <https://jinja.palletsprojects.com/en/2.11.x/api/#autoescaping>
