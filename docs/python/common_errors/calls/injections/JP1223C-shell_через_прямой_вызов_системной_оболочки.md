# JP1223C
## Проверка вызовов команд через системную оболочку shell

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

----

Создание внешних процессов через утилиты операционной системы требует повышенного контроля экранирования входных параметров. Вызов оболочки вызывает системную программу по выбору пользователя и зависит от платформы. Представляет собой уязвимость при наличии неэкранированного ввода команды, или невалидированного ввода фиксированной команды.

## Пример небезопасного использования

```python linenums="1"
import os

def your_echo(input: str):
    os.system(f"/bin/echo {input}")
```

## Проверяемые методы

* `os.system`
* `os.popen`
* `os.popen2`
* `os.popen3`
* `os.popen4`
* `popen2.popen2`
* `popen2.popen3`
* `popen2.popen4`
* `popen2.Popen3`
* `popen2.Popen4`
* `commands.getoutput`
* `commands.getstatusoutput`
* `subprocess.getoutput`
* `subprocess.getstatusoutput`

## Дополнительная информация

*  <https://cwe.mitre.org/data/definitions/78.html>
*  <https://docs.python.org/2/library/subprocess.html#frequently-used-arguments>
