# docs.jethub.pro

разработано на движке [mkdocs](https://github.com/squidfunk/mkdocs-material)

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
