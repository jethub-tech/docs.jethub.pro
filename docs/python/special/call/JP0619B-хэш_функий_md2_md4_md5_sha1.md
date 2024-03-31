# JP0619B
## Использование небезопасных хэш функций `md2`, `md4`, `md5`, or `sha1`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

----

Некоторые алгоритмы хэш-функций имеют слабую устойчивость к возникновений коллизий. Данный тест проверяет использование библиотечных функций, реализующих данные алгоритмы.

## Список вызовов

* `hashlib.md5`
* `hashlib.sha1`
* `Crypto.Hash.MD2.new`
* `Crypto.Hash.MD4.new`
* `Crypto.Hash.MD5.new`
* `Crypto.Hash.SHA.new`
* `Cryptodome.Hash.MD2.new`
* `Cryptodome.Hash.MD4.new`
* `Cryptodome.Hash.MD5.new`
* `Cryptodome.Hash.SHA.new`
* `cryptography.hazmat.primitives .hashes.MD5`
* `cryptography.hazmat.primitives .hashes.SHA1`

## Дополнительная информация

* <https://docs.python.org/3/library/hashlib.html>
* <https://pycryptodome.readthedocs.io/en/latest/src/hash/hash.html>
* <https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/>
