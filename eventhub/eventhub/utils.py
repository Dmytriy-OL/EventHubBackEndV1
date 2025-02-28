import urllib

from transliterate import translit
from unidecode import unidecode

def convert_name_to_url(text: str) -> str:

    transliterated = translit(text, 'ru', reversed=True)
    transliterated = unidecode(transliterated)
    # URL-енкодинг
    url_friendly = urllib.parse.quote(transliterated)
    return url_friendly