# JP0215A
## Использование `assert`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

----

> Особенности: Касается не тестовых примеров

Использование `assert` не рекомендуется, т.к. это может повлиять на устойчивость программы. Также `assert` удаляется при компиляции в оптимизированный байт-код, что приводит к удалению различных защит.

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/703.html>
* <https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement>
* <https://bugs.launchpad.net/juniperopenstack/+bug/1456193>
* <https://bugs.launchpad.net/heat/+bug/1397883>
