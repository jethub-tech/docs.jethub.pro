# JP0633B
## Использование небезопасных схем в urllib `urlopen`

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

Перечисленные методы позволяют работать с неполностью валидированными URL-ами, и потому требуют дополнительной проверки разработчиком.

## Список вызовов

* `urllib.request.urlopen`
* `urllib.request.urlretrieve`
* `urllib.request.URLopener`
* `urllib.request.FancyURLopener`
* `six.moves.urllib.request.urlopen`
* `six.moves.urllib.request.urlretrieve`
* `six.moves.urllib.request.URLopener`
* `six.moves.urllib.request.FancyURLopener`

## Дополнительная информация

* <https://docs.djangoproject.com/en/dev/ref/utils/#module-django.utils.safestring>
