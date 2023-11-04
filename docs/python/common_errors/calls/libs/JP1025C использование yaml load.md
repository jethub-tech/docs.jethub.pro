# JP1025C
## Использование yaml load
Использование PyYAML yaml.load не рекомендуется, так как позволяет загружать объекты из
недоверенных источников. Вместо этого рекомендцется использование yaml.safe_load.

---
Пример небезопасного использования:
```
import yaml
with open("example.yaml", "r") as stream:
    (yaml.load(stream))
```
---
> Дополнительная информация:
> <https://cwe.mitre.org/data/definitions/20.htm>
> <https://pyyaml.org/wiki/PyYAMLDocumentation>
---
* __Особенности:__ ...
* __Степень критичности:__ СРЕДНЯЯ
* __Достоверность определения:__ ВЫСОКАЯ