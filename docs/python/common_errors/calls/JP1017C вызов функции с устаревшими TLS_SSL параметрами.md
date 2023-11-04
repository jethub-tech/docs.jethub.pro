# JP1017C
## Вызов функции с устаревшими TLS_SSL параметрами

Проверка вызова функции с параметром, указывающим на использование устарвших заголовков
для протоколов SSL/TLS. Использует набор заголовков из стандартного пакета Python.

> Дополнительная информация:
> <https://docs.python.org/3/library/ssl.html>
> <https://cwe.mitre.org/data/definitions/327.html>
---
Список токенов:
<!---
NOTE!! НУЖНО РАСШИРИТЬ СПИСОК. Дополнить проверкой версии питона https://docs.python.org/3/library/ssl.html
-->

- PROTOCOL_SSLv2
- SSLv2_METHOD
- SSLv23_METHOD
- PROTOCOL_SSLv3
- PROTOCOL_TLSv1
- SSLv3_METHOD
- TLSv1_METHOD
- PROTOCOL_TLSv1_1
- TLSv1_1_METHOD
---

* __Особенности:__ ...
<!---
NOTE!! CHANGE TO HIGH
-->
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ СРЕДНЯЯ