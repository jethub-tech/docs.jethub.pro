# JP1221C 
## Проверка вызова модуля Subprocess c параметром Shell. Расширенный список вызовов
Создание внешних процессов через утилиты операционной системы с параметром shell=True требует повышенного контроля 
экранирования входных параметров. Вызов оболочки вызывает программу по выбору пользователя и зависит от платформы. 
В общем случае вызовов через оболочку c параметром shell=True следует избегать.

Для вызова команд с параметром shell=False отключено большинство стандратных функий оболочки shell, что снижает
вероятность уязвимости с внедрением сторонних команд.

---
Пример небезопасного использования:
```
from subprocess import Popen
def call_gcc(param: str):
    Popen(f'bin/gcc {param}', shell=True)
```
---
Проверяемые методы:
<!---
NOTE!! CHECK execute with timeout
-->

* subprocess.Popen 
* subprocess.call
* subprocess.check_call
* subprocess.check_output
* execute_with_timeout
---
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/78.html>
> <https://docs.python.org/2/library/subprocess.html#frequently-used-arguments>
---
* __Особенности:__ Shell=True
<!---
NOTE!! CHANGE TO HIGH-LOW
-->
---
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ