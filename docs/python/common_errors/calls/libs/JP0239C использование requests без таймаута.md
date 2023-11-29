# JP0239C
## Использование requests без проверки SSL сертификатов
Использование библиотеки requests требует установки таймаута соединений при работе вне тестовой среды.

---
Пример небезопасного использования:
```python linenums="1"
import requests

requests.get("https://example.com")  # timeout=None
```
---
> Дополнительная информация:
> <https://requests.readthedocs.io/en/latest/user/advanced/#timeouts>
---
* __Особенности:__ ...
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ
