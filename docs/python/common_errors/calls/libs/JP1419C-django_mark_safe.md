# JP1419C
## Вызов Django `mark_safe`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-yellow?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-red?style=for-the-badge)

Использование функции `mark_safe` исключает защиту по умолчанию от небезопасного пользовательского ввода внутри фреймворка Django, и (в общем случае) не рекомендуется. Надлежащие проверки входных параметров должны проводиться разработчиком.

## Пример небезопасного использования

```python linenums="1"
def function(url):
    html = f'<a href="{url}">{url}</a>'
    return mark_safe(html)
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/80.html>
* <https://docs.djangoproject.com/en/dev/ref/utils/#module-django.utils.safestring>
