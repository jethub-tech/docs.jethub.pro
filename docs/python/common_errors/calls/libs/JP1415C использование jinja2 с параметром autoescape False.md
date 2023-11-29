# JP1415C
## JP1415C использование jinja2 с параметром autoescape False
Использование фреймворка Jinja2 без параметра autoescape=True отключает безопасный ввод
HTML шаблонов и открывает уязвимость к XSS атакам. Jinja2 рекомендуется использовать с параметром
autoescape=True в явном виде.


---
Пример небезопасного использовани
```python linenums="1"
import jinja2

environment = jinja2.Environment(autoescape=False)
template = environment.from_string("Hello, {{ name }}!")
template.render(name="World")
```
---
> Дополнительная информация
> <https://cwe.mitre.org/data/definitions/94.html>
> <https://jinja.palletsprojects.com/en/2.11.x/api/#autoescaping>
---
* __Особенности:__ ...
* __Степень критичности:__ ВЫСОКАЯ
* __Достоверность определения:__ ВЫСОКАЯ
