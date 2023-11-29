# JP0229S
## Небезопасное использование временных tmp файлов или директорий
Следует избегать работы с временными директориями и файлами вручную, без использования стандартных
библиотечных функций, которые учитывают такое потенциально небезопасное поведение как предсказуемые
временные пути и наименования, некорректные права доступа и неполная очистка.

---
Проверяемые строки: ['/tmp', '/var/tmp']
<!---
Нужно доработать этот плагин, так как сейчас он просто
проверяет наличие ['/tmp', '/var/tmp', '/dev/shm']
-->

Пример небезопасного создания временного файла:

```python linenums="1"
import os
import tempfile

# This will most certainly put you at risk
tmp = os.path.join(tempfile.gettempdir(), filename)
if not os.path.exists(tmp):
    with open(tmp, "w") file:
        file.write("defaults")
```

Пример безопасного использования:

```python linenums="1"
import os
import tempfile

# Use the TemporaryFile context manager for easy clean-up
with tempfile.TemporaryFile() as tmp:
    # Do stuff with tmp
    tmp.write("stuff")
```
---
> Дополнительная информация:
> <https://security.openstack.org/guidelines/dg_using-temporary-files-securely.html>
> <https://cwe.mitre.org/data/definitions/377.html>
> <https://cwe.mitre.org/data/definitions/379.html>
> <https://cwe.mitre.org/data/definitions/459.html>
---
* __Особенности:__ ...
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ СРЕДНЯЯ
