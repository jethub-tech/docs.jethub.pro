# JP1229S
## SQL инъекция

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

> Особенности: для улучшения результата работы данного теста, используется вторичный фильтр результатов

Проверяется использование строк, содержащих типичные запросы SQL, и которые могут содержать неэкранированные параметры. Инъекции возможны в общем случае, если разработчик использует такие «сырые» запросы без надлежащего контроля со стороны приложения, или без использования библиотечных функций, которые как правило реализуют такой контроль (если иное не предусмотрено такими функциями см. JP1233C, JP1235C).

## Пример небезопасного использования

```python linenums="1"
sql = "UPDATE dbtable SET {values} WHERE {in_clause}".format(
    values=values,
    in_clause=in_clause,
)  # confidence LOW (not wrapped in 'execute' call)

cursor.execute("SELECT * FROM TEST WHERE ID = '%s'" % (id_1_param,))  # confidence MEDIUM as it is wrapped in 'execute' call
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/89.html>
* <https://www.owasp.org/index.php/SQL_Injection>
