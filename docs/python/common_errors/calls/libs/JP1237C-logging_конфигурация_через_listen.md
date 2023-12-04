# JP1237C
## Небезопасное использование logging с конфигурацией через `listen`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

Динамическая конфигурация логгера logging через интерфейс `logging.config.listen`, может представлять риск безопасности, если не установлен флаг `verify` для проверки подписи и/или включения шифрования соединения. В противном случае возможно исполнения недоверенного кода через `eval()`.

## Пример небезопасного использования

```python linenums="1"
t = logging.config.listen(port=1234)  # verify=None
```

## Дополнительная информация

* <https://docs.python.org/3/library/logging.config.html#logging.config.listen>

* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ
