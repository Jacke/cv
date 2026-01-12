"""Label translations for CV formatting."""

from typing import Literal

Lang = Literal["en", "ru"]

LABELS: dict[str, dict[str, str]] = {
    "en": {
        "email": "✉️ Email",
        "github": "⚒️ Github",
        "phone": "📞 Phone",
        "availability": "📖 Availability",
        "legal_entity": "💼 Legal entity",
        "tech": "Tech",
        "location": "📍 Location",
        "english": "🌍 English, Ukranian, Russian",
    },
    "ru": {
        "email": "✉️ Почта",
        "github": "⚒️ Github",
        "phone": "📞 Телефон",
        "availability": "📖 Доступность",
        "legal_entity": "💼 Юр. лицо",
        "tech": "Технологии",
        "location": "📍 Локация",
        "english": "🌍 Русский, Английский",
    },
}


def get_label(key: str, lang: Lang = "en") -> str:
    """Get translated label for a given key."""
    return LABELS.get(lang, LABELS["en"]).get(key, key)
