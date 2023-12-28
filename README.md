# docs.jethub.pro

используется движок [mkdocs](https://github.com/squidfunk/mkdocs-material)

- установить нужные библиотеки (лучше в отдельном виртуальном окружении)

    ```bash
    pip install -r requirements.txt
    ```

- для просмотра динамической промежуточной версии книги выполнить

    ```bash
    mkdocs serve --dirtyreload
    ```

    для просмотра книги перейти по предложенной ссылке

- [`./mkdocs.yml`](./mkdocs.yml) -- файл настройки среды, в том числе и навигации книги (по ключу `nav`)

- все текстовые файлы для книги расположены в [`./docs/`](./docs/) в соответствующих директориях

- на странице движка – [https://squidfunk.github.io/mkdocs-material/reference/](https://squidfunk.github.io/mkdocs-material/reference/) – имеются примеры стилистики (`sponsors only` не наш случай). меж тем

  - вместо `–` использовать `–` (`option` + `-` для macos)
  - рисунки в `.png` формате
  - примеры кода всегда содержат нумерацию строк
  - `«»` в простом тексте
  - избегать «мы»/«вы»/«вас»/«нас»/..
  - ..

<details><summary>значки</summary>
<p>

* степень критичности

** высокая
![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

**средняя
![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

** низкая
![Static Badge](https://img.shields.io/badge/%D0%A1%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)

----
* достоверность определения

** высокая
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B0%D1%8F-crimson?style=for-the-badge)

**средняя
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F-orange?style=for-the-badge)

** низкая
![Static Badge](https://img.shields.io/badge/%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B8%D0%B7%D0%BA%D0%B0%D1%8F-mediumblue?style=for-the-badge)

</p>
</details>