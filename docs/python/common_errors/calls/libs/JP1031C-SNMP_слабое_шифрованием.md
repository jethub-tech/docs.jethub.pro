# JP1031C
## Использование библиотеки `snmp` со слабым шифрованием

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

----

Проверка использования слабого шифрования в версиях `snmp` v3 или выше.

## Пример небезопасного использования

```python linenums="1"
from pysnmp.hlapi import SnmpEngine, getCmd, UsmUserData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity

iterator = getCmd(
    SnmpEngine(),
    UsmUserData("usr-none-none"),  # no auth, no privacy set
    UdpTransportTarget(("demo.snmplabs.com", 161)),
    ContextData(),
    ObjectType(ObjectIdentity("IF-MIB", "ifInOctets", 1))
)
```

## Дополнительная информация

* <https://pysnmp.readthedocs.io/en/latest/examples/hlapi/v3arch/asyncore/sync/manager/cmdgen/snmp-versions.html>
