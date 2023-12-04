# JP0837B
## Импорт библиотек с уязвимостью httpoxy

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

Уязвимость в CGI Web приложениях, позволяющая внедрять проксирование запросов. Соответствующие библиотеки не рекомендованы к использованию.


## Список проверяемых импортов:

* `wsgiref.handlers.CGIHandler`
* `twisted.web.twcgi.CGIScript`
* `twisted.web.twcgi.CGIDirectory`

## Дополнительная информация

* <https://docs.python.org/3/library/wsgiref.html>
* <https://docs.twistedmatrix.com/en/stable/api/twisted.web.twcgi.CGIScript.html>
