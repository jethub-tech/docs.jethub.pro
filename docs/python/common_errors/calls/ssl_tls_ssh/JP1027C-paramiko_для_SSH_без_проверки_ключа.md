# JP1027C
## Использование библиотеки paramiko для SSH-соединений без проверки ключа

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

Библиотека paramiko по умолчанию верифицирует ключ hostkey сервера. Использование `AutoAddPolicy` или `WarningPolicy` позволяет добавлять ключ сервера без верификации и открывает возможность для MITM атак с умышленной подменой доверенного хоста.

## Пример небезопасного использования

```python linenums="1"
import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.set_missing_host_key_policy(paramiko.WarningPolicy)
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/322.html>
* <https://docs.paramiko.org/en/3.3/api/client.html>
