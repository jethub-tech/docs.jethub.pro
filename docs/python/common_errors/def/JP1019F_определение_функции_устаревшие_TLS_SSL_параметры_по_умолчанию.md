# JP1019F
## Определение функции с устаревшими TLS/SSL параметрами по умолчанию

<!---NOTE!! CHANGE TO HIGH-->
![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-yellow?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-yellow?style=for-the-badge)

Проверка определения пользователем функции с параметром по-умолчанию, указывающим на использование устаревших заголовков для протоколов SSL/TLS. Использует набор заголовков из стандартного пакета Python.

<!---NOTE!! НУЖНО РАСШИРИТЬ СПИСОК.
Дополнить проверкой версии питона https://docs.python.org/3/library/ssl.html-->
## Список токенов

* PROTOCOL_SSLv2
* SSLv2_METHOD
* SSLv23_METHOD
* PROTOCOL_SSLv3
* PROTOCOL_TLSv1
* SSLv3_METHOD
* TLSv1_METHOD
* PROTOCOL_TLSv1_1
* TLSv1_1_METHOD

## Дополнительная информация

* <https://docs.python.org/3/library/ssl.html>
