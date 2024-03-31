# JP1033C
## Использование `json.load`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

----

Проверка использования `json.load`. Злоумышленник может воспользоваться данной конструкцией для загрузки файла большого размера, что может привести к чрезмерному использованию системных ресурсов.

Достоверное определение размера файла не представляется возможным на этапе сканирования, поэтому рекомендуется использование динамической проверки параметров загружаемого файла и использование директивы `#nosec`. В качестве альтернативы предлагается ипользование последовательных json парсеров, таких как `ijson`, `ujosn` и т.п..

## Пример небезопасного использования

```python linenums="1"
import json

_file = open("large-file.json", "r")
data = json.load(_file)
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/502.html>
* <https://docs.python.org/3/library/json.html>
