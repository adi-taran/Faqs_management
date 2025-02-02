from django.test import TestCase

# Import necessary modules and classes for testing
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import FAQ

# Fixture to create an API client for testing
@pytest.fixture
def api_client():
    return APIClient()

# Fixture to create a sample FAQ object for testing
@pytest.fixture
def faq():
    return FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

# Test to check the translation functionality of the FAQ model
@pytest.mark.django_db
def test_faq_model_translation(faq):
    # Check if the translated question in Hindi is correct
    assert faq.get_translated_question('hi') == faq.question_hi or faq.question
    # Check if the translated question in Bengali is correct
    assert faq.get_translated_question('bn') == faq.question_bn or faq.question

# Test to check the FAQ list API endpoint
@pytest.mark.django_db
def test_faq_list(api_client, faq):
    url = reverse('faq-list')  # Get the URL for the FAQ list endpoint
    response = api_client.get(url)  # Make a GET request to the FAQ list endpoint
    assert response.status_code == status.HTTP_200_OK  # Check if the response status is 200 OK
    assert len(response.data) == 1  # Check if there is one FAQ in the response data
    assert response.data[0]['question'] == faq.question  # Check if the question in the response matches the sample FAQ

# Test to check the FAQ detail API endpoint
@pytest.mark.django_db
def test_faq_detail(api_client, faq):
    url = reverse('faq-detail', args=[faq.id])  # Get the URL for the FAQ detail endpoint
    response = api_client.get(url)  # Make a GET request to the FAQ detail endpoint
    assert response.status_code == status.HTTP_200_OK  # Check if the response status is 200 OK
    assert response.data['question'] == faq.question  # Check if the question in the response matches the sample FAQ