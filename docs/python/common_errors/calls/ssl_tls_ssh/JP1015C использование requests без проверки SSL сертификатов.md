# JP1015C
## Использование requests без проверки SSL сертификатов
Использование библиотеки requests требует использования флага verify=True для валидации
SSL сертификатов протокола HTTPS при работе вне тестовой среды.


---
Пример небезопасного использования:
```python linenums="1"
import requests

requests.get("https://example.com", verify=False)
```
---
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/295.html>
> <https://requests.readthedocs.io/en/latest/user/advanced/>
---
* __Особенности:__ ...
* __Степень критичности:__ ВЫСОКАЯ
* __Достоверность определения:__ ВЫСОКАЯ
