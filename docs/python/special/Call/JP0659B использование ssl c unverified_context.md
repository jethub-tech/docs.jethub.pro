# JP0659B
## Использование ssl c unverified_context
Принудительное использование ssl._create_unverified_context небезопасно,
так как избегает валидации сертификатов и проверки хостов.


---
Список вызовов:

* ssl._create_unverified_context

---
> Дополнительная информация:
> <https://docs.python.org/3/library/http.client.html?highlight=unverified_context>
---
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ