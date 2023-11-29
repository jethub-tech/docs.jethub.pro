# JP0619B
## Использование небезопасных хэш функций MD2, MD4, MD5, or SHA1
Некоторые алгоритмы хэш-функций имеют слабую устойчивость к возникновений коллизий.
Данный тест проверяет использование библиотечных функций, реализующих данные алгоритмы.

---
Список вызовов:

* hashlib.md5
* hashlib.sha1
* Crypto.Hash.MD2.new
* Crypto.Hash.MD4.new
* Crypto.Hash.MD5.new
* Crypto.Hash.SHA.new
* Cryptodome.Hash.MD2.new
* Cryptodome.Hash.MD4.new
* Cryptodome.Hash.MD5.new
* Cryptodome.Hash.SHA.new
* cryptography.hazmat.primitives .hashes.MD5
* cryptography.hazmat.primitives .hashes.SHA1

---
> Дополнительная информация:
> <https://docs.python.org/3/library/hashlib.html>
> <https://pycryptodome.readthedocs.io/en/latest/src/hash/hash.html>
> <https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/>
---
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ
