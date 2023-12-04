# JP1015C
## Использование requests без проверки SSL сертификатов

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

Использование библиотеки requests требует использования флага `verify=True` для валидации SSL сертификатов протокола HTTPS при работе вне тестовой среды.

## Пример небезопасного использования

```python linenums="1"
import requests

requests.get("https://example.com", verify=False)
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/295.html>
* <https://requests.readthedocs.io/en/latest/user/advanced/>
