from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    """
    Serializer for the FAQ model.

    This serializer converts FAQ model instances into JSON format and vice versa.
    It includes the following fields:
    - id: The unique identifier for the FAQ.
    - question: The question text of the FAQ.
    - answer: The answer text of the FAQ.

    Meta:
        model (FAQ): The model that is being serialized.
        fields (list): The list of fields to be included in the serialization.
    """
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']
    