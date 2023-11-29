# JP1031C
## Использование библиотеки SNMP со слабым шифрованием
Проверка использования слабого шифрования в версиях SNMP v3 или выше.

---
Пример небезопасного использовани
```python linenums="1"
from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    UsmUserData("usr-none-none"),  # no auth, no privacy set
    UdpTransportTarget(("demo.snmplabs.com", 161)),
    ContextData(),
    ObjectType(ObjectIdentity("IF-MIB", "ifInOctets", 1))
)
```
---
> Дополнительная информация
> <https://pysnmp.readthedocs.io/en/latest/examples/hlapi/v3arch/asyncore/sync/manager/cmdgen/snmp-versions.html>
---
* __Особенности:__ ...
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ
