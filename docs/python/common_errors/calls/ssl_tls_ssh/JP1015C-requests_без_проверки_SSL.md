# JP1015C
## Использование `requests, httpx, httplib2` без проверки SSL сертификатов

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

----

Использование библиотеки `requests`, `httpx`, `httplib2`, `urllib3` с `verify=False`,`disable_ssl_certificate_validation=False, urllib3.disable_warnings()` отключает валидацию SSL сертификатов протокола HTTPS, что небезопасно при подключении к серверу вне тестовой среды.

## Пример небезопасного использования

```python linenums="1"
import requests

requests.get("https://example.com", timeout=30, verify=False)
requests.post("https://gmail.com", timeout=30, verify=False)
requests.put("https://gmail.com", timeout=30, verify=False)
requests.delete("https://gmail.com", timeout=30, verify=False)
requests.patch("https://gmail.com", timeout=30, verify=False)
requests.options("https://gmail.com", timeout=30, verify=False)
requests.head("https://gmail.com", timeout=30, verify=False)

import httpx



httpx.get("https://example.com", timeout=30, verify=False)
httpx.post("https://gmail.com", timeout=30, verify=False)
httpx.put("https://gmail.com", timeout=30, verify=False)
httpx.delete("https://gmail.com", timeout=30, verify=False)
httpx.patch("https://gmail.com", timeout=30, verify=False)
httpx.options("https://gmail.com", timeout=30, verify=False)
httpx.head("https://gmail.com", timeout=30, verify=False)
httpx.Client(verify=False)
httpx.AsyncClient(verify=False)

import httplib2

h = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
resp, content = h.request("https://github.com/", "POST")

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/295.html>
* <https://requests.readthedocs.io/en/latest/user/advanced/>
