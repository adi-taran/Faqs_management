from googletrans import Translator
from googletrans import LANGUAGES
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Initialize the translator
translator = Translator()

def translate_text(lang: str, text: str, retries=3) -> str:
    """
    Translate the given text to the specified language.

    Parameters:
    lang (str): The target language code.
    text (str): The text to be translated.
    retries (int): Number of retry attempts in case of failure.

    Returns:
    str: Translated text or original text if translation fails.
    """
    # Check if the target language is supported
    if lang not in LANGUAGES:
        return f"Error: Unsupported language '{lang}'"

    # Initialize the translator
    translator = Translator()
    
    # Attempt to translate the text, retrying if necessary
    for attempt in range(retries):
        try:
            # Perform the translation
            translation = translator.translate(text, dest=lang)
            return translation.text
        except Exception as e:
            # Log the error
            logger.error(f"Translation Error ({lang}): {e}")
            if attempt < retries - 1:
                continue  # Retry if attempts are left
            return text  # Fallback to original text if translation fails