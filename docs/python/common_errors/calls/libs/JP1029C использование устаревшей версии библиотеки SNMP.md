# JP1029C
## Использование устаревшей версии библиотеки SNMP
Проверка использования устаревших версий SNMP ниже v3. 


---
Пример небезопасного использования:
```
from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('demo.snmplabs.com', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
)
```
---
> Дополнительная информация:
> <https://pysnmp.readthedocs.io/en/latest/examples/hlapi/v3arch/asyncore/sync/manager/cmdgen/snmp-versions.html>
---
* __Особенности:__ ...
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ