# JP1215C
## Shell инъекция. Небезопасное использование `paramiko`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

----

Запуск команд ОС через удаленное соединения с использованием библиотеки `paramiko`, может представлять риск безопасности, без надлежащей проверки информации на входе разработчиком.  

## Пример небезопасного использования

```python linenums="1"
import paramiko

paramiko.exec_command("command to be sanitized by developer")
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/78.html>
* <https://github.com/paramiko/paramiko>
