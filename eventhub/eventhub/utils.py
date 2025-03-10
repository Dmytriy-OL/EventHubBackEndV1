from unidecode import unidecode
import urllib.parse

CYRILLIC_TO_LATIN = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo",
    "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch",
    "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya"
}

def transliterate(text: str) -> str:
    return "".join(CYRILLIC_TO_LATIN.get(c, c) for c in text.lower())

def convert_name_to_url(text: str) -> str:
    transliterated = transliterate(text)
    transliterated = unidecode(transliterated)
    url_friendly = urllib.parse.quote(transliterated)
    return url_friendly
