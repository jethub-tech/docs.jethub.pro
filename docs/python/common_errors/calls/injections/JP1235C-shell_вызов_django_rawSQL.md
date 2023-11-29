# JP1235C
## Проверка вызова Django `RawSQL`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-yellow?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-yellow?style=for-the-badge)

Использование функции `RawSQL` исключает защиту от инъекций внутри фреймворка Django, и (в общем случае) не рекомендуется. Надлежащие проверки входных параметров должны проводиться разработчиком.

## Пример небезопасного использования

```python linenums="1"
from django.db.models.expressions import RawSQL

queryset.annotate(val=RawSQL(f"select col from sometable where othercol = '{param}'"))
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/89.html>
* <https://docs.djangoproject.com/en/dev/ref/models/expressions/#django.db.models.expressions.RawSQL>
