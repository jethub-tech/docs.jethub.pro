# JP1027C
## Использование библиотеки paramiko для SSH-соединений без проверки ключа
Библиотека paramiko по умолчанию верифицирует ключ hostkey сервера. Использование
AutoAddPolicy или WarningPolicy позволяет добавлять ключ сервера без верификации и открывает
возможность для MITM атак с умышленной подменой доверенного хоста.

---
Пример небезопасного использования:
```python linenums="1"
import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.set_missing_host_key_policy(paramiko.WarningPolicy)
```
---
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/322.html>
> <https://docs.paramiko.org/en/3.3/api/client.html>
---
* __Особенности:__ ...
* __Степень критичности:__ ВЫСОКАЯ
* __Достоверность определения:__ СРЕДНЯЯ
