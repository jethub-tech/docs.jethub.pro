# JP1417C
## Использование `mako` без самостоятельной проверки ввода

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

----

Использование фреймворка `mako` без самостоятельной проверки ввода HTML шаблонов и открывает уязвимость к XSS атакам. Требуется убедиться, что выходные шаблоны надлежащим образом экранированы с использованием флагов `n`, `h` или `x` (например, для переменной `temp: ${ temp |h }`).

## Пример небезопасного использования

```python linenums="1"
import mako

mako.template.Template("my_template")
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/80.html>
* <https://www.makotemplates.org/>
