# JP1223C
## Проверка вызовов команд через системную оболочку Shell
Создание внешних процессов через утилиты операционной системы требует повышенного контроля
экранирования входных параметров. Вызов оболочки вызывает системную программу по выбору пользователя и
зависит от платформы. Представляет собой уязвимость при наличии неэкранированного ввода команды, или невалидированного
ввода фиксированной команды.


---
Пример небезопасного использования:
```
def your_echo(input: str):
    os.system(f'/bin/echo {input}')
```
---
Проверяемые методы:
* os.system
* os.popen
* os.popen2
* os.popen3
* os.popen4
* popen2.popen2
* popen2.popen3
* popen2.popen4
* popen2.Popen3
* popen2.Popen4
* commands.getoutput
* commands.getstatusoutput
---
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/78.html>
> <https://docs.python.org/2/library/subprocess.html#frequently-used-arguments>
---
* __Особенности:__ ...
---
* __Степень критичности:__ НИЗКАЯ
* __Достоверность определения:__ СРЕДНЯЯ
