# JP1037C
## Использование стандартных библиотек для записи в csv файл без дополнительной валидации

![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

Проверка использования `numpy.savetxt`, `dataframe.to_csv` и `csvWriter.writerow`.
Злоумышленник может воспользоваться данными функциями для записи непроверенных данных в csv файл,
что может привести к запуску вредоносного кода при последующем открытии такого файла на целевой машине.


Для переменной, содержащей csv данные для записи в файл, дополнительно сканируется контекст текущей функции на наличие пользовательской проверки в явном виде,
например, функции содержащей в своем заголовке таких ключевых слов как `preprocess`, `check`, `sanitize`, `verify`.
Сканер определяет как ошибку те случаи, для которых такие методы не найдены,
и переменная с csv данными берется напрямую из аргументов текущей функции или из входящего запроса типа request.

Проверка содержимого входных данных невозможна на этапе сканирования,
поэтому рекомендуется использование проверочной функции, содержащей в заголовке такие ключевые слова как `preprocess`, `check`, `sanitize`, `verify`
для валидации входных данных.

Если такой подход представляется избыточным для конкретного случая, то рекомендуется использование директивы `#nosec` для подавления ошибки.

## Проверяемые методы

* `numpy.savetxt`
* `dataframe.to_csv`
* `csvWriter.writerow`

## Пример небезопасного использования

```python linenums="1"
# CONFIDENCE = LOW
@app.route('/bad')
def csv_store_with_writerow_bad(csv_data):
    # csv_data input to writerow not sanitized
    csvWriter = csv.writer(open("test.csv", "wt"))
    csvWriter.writerow(func(csv_data, sanitize(var1)))

    return 1
```

```python linenums="1"
# CONFIDENCE = LOW
def csv_store_with_numpy_bad(data_np_array):
    # this is considered bad as it is from func argument
    filename = 'data.csv'
    np.savetxt(filename, data_np_array, delimiter=',', fmt='%s')
```

```python linenums="1"
# CONFIDENCE = MEDIUM
@app.route('/bad')
def bad_request():
    # csv_data comes from request and not sanitized
    csv_data = request.args.get('csv')
    csvWriter = csv.writer(open("test.csv", "wt"))
    csvWriter.writerow(func(csv_data, sanitize(var1)))

    return 1
```



## Пример безопасного использования

```python linenums="1"
@app.route('/good')
def csv_store_with_writerow_good(csv_data):
    # inputs to writerow are wrapped with sanitize
    csvWriter = csv.writer(open("test.csv", "wt"))
    csvWriter.writerow(func(sanitize(csv_data, var1)))

    return "good"
```

```python linenums="1"
def csv_store_with_numpy_good(data_np_array):
    # this is considered bad as it is from func argument
    filename = 'data.csv'
    np.savetxt(filename, verify_input(data_np_array), delimiter=',', fmt='%s')
```

```python linenums="1"
def good_preprocess_in_context(csv_input_bad):
    # inputs to wrtierow are covered with sanitize in preprocess
    print("Writing sanitized")
    csv_input_good = preprocess(csv_input_bad, ARGS)  # some sanitize method
    csvWriter = csv.writer(open("test.csv", "wt"))
    csvWriter.writerow(csv_input_good)
```

## Дополнительная информация

* <https://cwe.mitre.org/data/definitions/1236.html>
* <https://docs.python.org/3/library/csv.html>
