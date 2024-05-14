# JP0659B
## Использование `ssl` c `unverified_context`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

----

Принудительное использование `ssl._create_unverified_context` небезопасно, так как избегает валидации сертификатов и проверки хостов.
Стоит отметить, что модуль `ssl` используется такими модулями python для работы с http соединениями как `http.client`, `httplib` или `urllib2`

## Пример небезопасного использования

```python linenums="1"
from urllib.request import urlopen
import ssl

response = urlopen("https://example.org", context=ssl._create_unverified_context())

import http.client
import ssl

context = ssl._create_unverified_context()
conn = http.client.HTTPSConnection("example.com", context=context)
conn.request("GET", "/")


import httplib
import ssl

context = ssl._create_unverified_context()
conn = httplib.HTTPSConnection("example.com", context=context)
conn.request("GET", "/")
```

## Дополнительная информация

* <https://docs.python.org/3/library/http.client.html?highlight=unverified_context>
