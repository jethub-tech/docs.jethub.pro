# JP1225C
## Проверка создания процесса через методы `os` без использования shell

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

----

Как правило, ошибка не представляет собой уязвимость, так как создаваемый процесс не использует оболочку shell, а подменяет вызывающий. Тем не менее данный тест рекомендован к использованию для индикации потенциально уязвимых мест программы в рамках тестирования (на проникновение).

## Пример небезопасного использования

```python linenums="1"
import os

os.spawnv(mode, path, args)
```

## Проверяемые методы

* `os.execl`
* `os.execle`
* `os.execlp`
* `os.execlpe`
* `os.execv`
* `os.execve`
* `os.execvp`
* `os.execvpe`
* `os.spawnl`
* `os.spawnle`
* `os.spawnlp`
* `os.spawnlpe`
* `os.spawnv`
* `os.spawnve`
* `os.spawnvp`
* `os.spawnvpe`
* `os.startfile`

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/78.html>
* <https://docs.python.org/3/library/os.html#os.system>
