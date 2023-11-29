# JP0633B
## Использование небезопасных схем в urllib urlopen
Перечисленные методы позволяют работать с неполностью валидированными URL'ами, и потому требуют
дополнительной проверки разработчиком.

---
Список вызовов:

* urllib.request.urlopen
* urllib.request.urlretrieve
* urllib.request.URLopener
* urllib.request.FancyURLopener
* six.moves.urllib.request.urlopen
* six.moves.urllib.request.urlretrieve
* six.moves.urllib.request.URLopener
* six.moves.urllib.request.FancyURLopener

---
> Дополнительная информация:
> <https://docs.djangoproject.com/en/dev/ref/utils/#module-django.utils.safestring>
---
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ
