# JP0837B
## Импорт библиотек с уязвимостью httpoxy
Уязвимость в CGI Web приложениях, позволяющая внедрять проксирование запросов.
Соответствующие библиотеки не рекомендованы к использованию.


---
Список проверяемых импортов:

* wsgiref.handlers.CGIHandler 
* twisted.web.twcgi.CGIScript 
* twisted.web.twcgi.CGIDirectory

---
> Дополнительная информация:
> <https://docs.python.org/3/library/wsgiref.html>
> <https://docs.twistedmatrix.com/en/stable/api/twisted.web.twcgi.CGIScript.html>
---
* __Степень критичности:__ ВЫСОКАЯ
* __Достоверность определения:__ ВЫСОКАЯ