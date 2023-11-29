# JP1235C
## Проверка вызова Django RawSQL
Использование функции RawSQL исключает защиту от инъекций внутри фреймворка Django,
и, в общем случае, не рекомендуется. Надлежащие проверки входных параметров должны проводиться
разработчиком.


---
Пример небезопасного использования:
```
from django.db.models.expressions import RawSQL
queryset.annotate(val=RawSQL("select col from sometable where othercol = '%s'" % (param, )))
```
---
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/89.html>
> <https://docs.djangoproject.com/en/dev/ref/models/expressions/#django.db.models.expressions.RawSQL>
---
* __Особенности:__ ...
---
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ СРЕДНЯЯ
