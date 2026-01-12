# Curriculum Vitae
*Tempora mutantur, et nos mutamur in illis.*

<p align="center">
  <img src="./logo.png" alt="CV Apply Logo" width="720"/>
</p>

**English:** Times change, and we change with them.  
**Русский:** Времена меняются, и мы меняемся вместе с ними.  
**한국어:** 시간은 흐르고 우리도 그 속에서 변해간다.

---

# CV Apply Package

Модульная система для применения структурированных CV данных к шаблонам Google Docs.

## Структура модулей

### `constants.py`
Константы, используемые в системе:
- Маркеры буллетов для разных секций
- Регулярные выражения для обнаружения URL, email, телефонов
- Заголовки секций и ландмарки блоков
- OAuth scope'ы для Google Docs API

### `utils.py`
Вспомогательные функции общего назначения:
- Чтение/запись JSON файлов
- Нормализация текста и списков
- Логирование с таймстампами
- Извлечение плейсхолдеров

### `formatters.py`
Форматирование секций CV:
- `format_summary()` - форматирование резюме
- `format_skills()` - форматирование навыков
- `format_experiences()` - форматирование опыта работы (разделяет обычный опыт и предпринимательство)
- `format_education()` - форматирование образования
- `format_publications()` - форматирование публикаций
- `build_replacements()` - построение полного словаря замен

### `document.py`
Операции с документами:
- Парсинг ссылок на Google Docs
- Извлечение ID документа из URL
- Итерация по параграфам документа
- Поиск секций по заголовкам
- Создание запросов для создания ссылок (auto-linkify)

### `styling.py`
Стилизация документов:
- `style_skills_section()` - стилизация секции навыков
- `style_experience_section()` - стилизация секций опыта
- `apply_block_styles()` - применение всех стилей к документу

### `state.py`
Управление состоянием:
- Чтение/запись файла состояния
- Обновление состояния после применения
- Инвертирование словаря замен для reset операций

### `cli.py`
CLI утилиты для взаимодействия с gdocs_cli:
- `apply_with_auto_auth()` - применение замен с авто-реаутентификацией
- `get_doc_text()` - получение текста документа
- `needs_reauth()` - проверка необходимости повторной аутентификации

### `reset.py`
Операции сброса документа:
- `reset_document()` - сброс документа к плейсхолдерам

## Использование

### Основной скрипт

```bash
# Применить CV данные к документу
./cv_structured_apply_refactored.py --data data/cv.json --doc "CV Template"

# Только сгенерировать JSON с заменами
./cv_structured_apply_refactored.py --data data/cv.json --out replacements.json

# Сбросить документ к плейсхолдерам
./cv_structured_apply_refactored.py --reset --doc "CV Template"

# Dry run (без изменения документа)
./cv_structured_apply_refactored.py --data data/cv.json --doc "CV Template" --dry-run