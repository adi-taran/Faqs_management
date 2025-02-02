from django.db import models, transaction
from ckeditor.fields import RichTextField
from .redis_handler import RedisHandler
from googletrans import LANGUAGES
from .utils import translate_text

# Initialize Redis handler
redis_handler = RedisHandler()

class FAQ(models.Model):
    # Define language choices for translation
    LANGUAGE_CHOICES = [
        'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs',
        'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs',
        'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl',
        'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi',
        'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn',
        'kk', 'km', 'ko', 'ku', 'ky', 'la', 'lv', 'lt', 'lb',
        'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne',
        'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm',
        'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es',
        'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur',
        'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
    ]
    
    # Define model fields
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor for answer
    question_translated = models.JSONField(default=dict, blank=True)
    answer_translated = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Use atomic transaction to ensure data integrity
        with transaction.atomic():
            if not self.pk:
                self.translate_content()  # Translate content if it's a new FAQ

            super().save(*args, **kwargs)

            # Cache the FAQ in Redis
            cache_key = f"faq:{self.pk}"
            faq_data = {
                "id": self.pk,
                "question": self.question,
                "answer": self.answer,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "question_translated": self.question_translated,
                "answer_translated": self.answer_translated,
            }
            redis_handler.set_cache_with_transaction(cache_key, faq_data)

    def translate_content(self):
        # Translate question and answer to all languages in LANGUAGE_CHOICES
        try:
            for lang in self.LANGUAGE_CHOICES:
                if lang != "en": 
                    self.question_translated[lang] = str(translate_text(lang, self.question))
                    self.answer_translated[lang] = str(translate_text(lang, self.answer))
        except Exception as e:
            print(f"Translation failed: {e}")

    def get_translated_question(self, lang='en'):
        # Get translated question for the specified language
        return self.question_translated.get(lang, self.question)

    def get_translated_answer(self, lang='en'):
        # Get translated answer for the specified language
        return self.answer_translated.get(lang, self.answer)

    def __str__(self):
        # String representation of the FAQ
        return self.question
