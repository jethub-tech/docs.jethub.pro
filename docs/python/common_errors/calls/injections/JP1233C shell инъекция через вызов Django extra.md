# JP1233C 
## Проверка вызова Django extra
Использование функции extra исключает защиту от инъекций внутри фреймворка Django,
и, в общем случае, не рекомендуется. Надлежащие проверки входных параметров должны проводиться 
разработчиком.


---
Пример небезопасного использования:
```
qs.extra(select={"val": "select col from sometable where othercol = '%s'" % (param,)})
```
---
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/89.html>
> <https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.extra>
---
* __Особенности:__ ...
---
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ СРЕДНЯЯ