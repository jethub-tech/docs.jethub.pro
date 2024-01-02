# JP0229S
## Небезопасное использование временных tmp файлов или директорий

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

<!---Нужно доработать этот плагин, так как сейчас он просто проверяет наличие ['/tmp', '/var/tmp', '/dev/shm']-->

Следует избегать работы с временными директориями и файлами вручную, без использования стандартных библиотечных функций, которые учитывают такое потенциально небезопасное поведение как предсказуемые временные пути и наименования, некорректные права доступа и неполная очистка.

## Проверяемые строки

* `/tmp`
* `/var/tmp`

## Пример небезопасного создания временного файла

```python linenums="1"
with open("/var/tmp/123", "w") as f:
    f.write("def")
```

## Пример безопасного использования

```python linenums="1"
import os
import tempfile

with tempfile.TemporaryFile() as tmp:
    tmp.write("stuff")
```

## Дополнительная информация

* <https://security.openstack.org/guidelines/dg_using-temporary-files-securely.html>
* <https://cwe.mitre.org/data/definitions/377.html>
* <https://cwe.mitre.org/data/definitions/379.html>
* <https://cwe.mitre.org/data/definitions/459.html>
