# JP1231C
## Использование wildcard символа при вызове команд ОС
Использование wildcard * символа от привилегированного аккаунта представляет собой уязвимость, в
частности при использовании с командами, которые имеют потенциально небезопасные флаги.

<!---
НУЖНО проверить работоспоспособность данного теста после переработки
-->
---
Проверяются следующие команды:

* 'chown'
* 'chmod'
* 'tar'
* 'rsync'

Список вызовов:

* subprocess.Popen
* subprocess.call
* os.system
* os.popen
* popen2.Popen3
* popen2.Popen4
* commands.getoutput
* commands.getstatusoutput
* os.execl
* os.execle
---
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/78.html>
> <https://materials.rangeforce.com/tutorial/2019/11/08/Linux-PrivEsc-Wildcard/>
---
* __Особенности:__ ...
* __Степень критичности:__ ВЫСОКАЯ
* __Достоверность определения:__ СРЕДНЯЯ
