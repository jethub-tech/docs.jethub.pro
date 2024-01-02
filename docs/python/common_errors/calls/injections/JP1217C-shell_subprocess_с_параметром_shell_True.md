# JP1217C
## Проверка вызова модуля `subprocess` c параметром `shell`

<!---
NOTE!! CHANGE TO HIGH-LOW
-->
![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

> Особенности: `Shell=True`

Создание внешних процессов через утилиты операционной системы с параметром `shell=True` требует повышенного контроля экранирования входных параметров. Вызов оболочки вызывает программу по выбору пользователя и зависит от платформы. В общем случае вызовов через оболочку c параметром `shell=True` следует избегать.

Для вызова команд с параметром `shell=False` отключено большинство стандартных функций оболочки shell, что снижает вероятность уязвимости с внедрением сторонних команд.

## Проверяемые методы

* `subprocess.Popen`
* `subprocess.call`

## Дополнительная информация

* <https://docs.python.org/2/library/subprocess.html#frequently-used-arguments>
