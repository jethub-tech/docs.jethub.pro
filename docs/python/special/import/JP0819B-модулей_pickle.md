# JP0819B
## Импорт модулей `pickle`

<!-- сделать:  изменить на высокую -->
![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

----

Использование `pickle` может быть небезопасным при десериализации данных из недоверенного источника. Существует возможность создания таких объектов, которые могут вызвать проблемный код на исполнение в процессе десериализации. Данный тест предупреждает как о прямом использовании `pickle`, так и об использовании функций из нескольких общеизвестных библиотек, которые сами используют `pickle`.

## Список проверяемых импортов

* `pickle`
* `cPickle`
* `dill`
* `shelve`

## Дополнительная информация

* <https://docs.python.org/3/library/pickle.html>
* <https://lwn.net/Articles/964392/>
