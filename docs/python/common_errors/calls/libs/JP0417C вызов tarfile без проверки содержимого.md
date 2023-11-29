# JP0417C
## JP0417C вызов tarfile без проверки содержимого
Использование функции tarfile.extractall без валидации содержимого с указанием
проверяющей функции.


---
Пример небезопасного использования:
```
tarfile.extractall()
tarfile.extractalll(members=function(tarfile))
```
---
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/22.html>
> <https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall>
---
* __Особенности:__ в новых версиях библиотеки tarfile начиная с 3.12 добавлено
использование стандартных фильтров через параметр filter.
* __Степень критичности:__ НИЗКАЯ-ВЫСОКАЯ
* __Достоверность определения:__ ВЫСОКАЯ
