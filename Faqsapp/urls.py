from django.urls import path
from .views import FAQList, FAQDetail  # Importing the class-based views for FAQ list and detail

urlpatterns = [
    # URL pattern for the FAQ list view
    path('faqs/', FAQList.as_view(), name='faq-list'),
    
    # URL pattern for the FAQ detail view, expecting an integer primary key
    path('faqs/<int:pk>/', FAQDetail.as_view(), name='faq-detail'),
    
    # The following lines are commented out as they are not currently in use
    # URL pattern for the FAQ list function-based view
    # path('faq/', faq_list, name='faq-list'),
    
    # URL pattern for the FAQ detail function-based view, expecting an integer primary key
    # path('faq/<int:pk>/', faq_detail, name='faq-detail'),
]
