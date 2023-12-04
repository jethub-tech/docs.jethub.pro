# JP0237E
## Блок try-except с использованием continue

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-red?style=for-the-badge)

> Особенности: проверка дочерних исключений (typed_exception) может быть отключена

Игнорирование исключения с использованием ключевого слова `сontinue` может представлять уязвимость в общем случае, прежде всего при использовании базового класса `except Exception`.

## Пример небезопасного использования

```python linenums="1"
try:
  f()
except Exception:
  continue
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/703.html>
