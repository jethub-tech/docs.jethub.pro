# JP1225С
## Проверка создания процесса через методы os без использования shell.
Как правило, ошибка не представляет собой уязвимость, так как создаваемый процесс не
использует оболочку shell, а подменяет вызывающий.
Тем не менее данный тест реконендован к использованию 
для индикации потенциально уязвимых мест программы в 
рамках тестирования (на проникновение).

---
Пример небезопасного использования:
```
import os
os.spawnv(mode, path, args)
```
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
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/78.html>
> <https://docs.python.org/3/library/os.html#os.system>
---
* __Особенности:__
---
* __Степень критичности:__ НИЗКАЯ
* __Достоверность определения:__ СРЕДНЯЯ