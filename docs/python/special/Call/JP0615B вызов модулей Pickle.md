# JP0615B
## Вызов модулей Pickle
Использование pickle может быть небезопасным при десериализации данных из недоверенного источника.
Существует возможность создания pickle объектов, которые могут вызвать проблемный код
на исполнение в процессе десериализации.
Данный тест предупреждает как о прямом использовании pickle, так и об использовании функций из нескольких
общеизвестных библиотек, которые сами используют pickle.

---
Список вызовов:

* pickle.loads
* pickle.load
* pickle.Unpickler
* dill.loads
* dill.load
* dill.Unpickler
* shelve.open
* shelve.DbfilenameShelf
* jsonpickle.decode
* jsonpickle.unpickler.decode
* jsonpickle.unpickler.Unpickler
* pandas.read_pickle
---
> Дополнительная информация:
> <https://docs.python.org/3/library/pickle.html>
---
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ
