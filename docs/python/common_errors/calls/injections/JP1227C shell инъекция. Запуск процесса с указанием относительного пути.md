# JP 1227С
## JP1227C shell инъекция. Запуск процесса с указанием относительного пути

Проверка использования относительного при запуске нового процесса (использование 
пути, который не начинается с символа '/').
В случае умышленной подмены переменных окружения в файле PATH, 
может быть потенциально запущена небезопасная программа.

> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/78.html>
> <https://docs.python.org/3/library/os.html#os.system>
---
Проверяемые методы:

* os.execl
* os.execle
* os.execlp
* os.execlpe
* os.execv
* os.execve
* os.execvp
* os.execvpe
* os.spawnl
* os.spawnle
* os.spawnlp
* os.spawnlpe
* os.spawnv
* os.spawnve
* os.spawnvp
* os.spawnvpe
* os.startfile
---

* __Особенности:__

* __Степень критичности:__ НИЗКАЯ
* __Достоверность определения:__ СРЕДНЯЯ