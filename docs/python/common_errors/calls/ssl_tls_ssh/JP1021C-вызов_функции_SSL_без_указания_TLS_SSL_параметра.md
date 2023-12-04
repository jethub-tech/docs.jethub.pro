# JP1021C
## Вызов функции SSL без указания TLS_SSL параметра

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-yellow?style=for-the-badge)

<!---NOTE!! НУЖНО ПРОВЕРИТЬ РАБОТУ ТАК КАК ИСПОЛЬЗУЕТСЯ КОНФИГ из ssl_with_bad_version-->

Проверка вызова функции `ssl.wrap_socket()` без параметра, указывающего на требуемый протокол SSL/TLS.

## Дополнительная информация

* <https://docs.python.org/3/library/ssl.html>
* <https://cwe.mitre.org/data/definitions/327.html>
