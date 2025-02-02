from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

# Define a custom form for the FAQ model to use CKEditor for the answer field
class FAQAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FAQ
        fields = '__all__'

# Register the FAQ model with the custom admin interface
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question', 'get_translated_question', 'get_translated_answer', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    list_filter = ('created_at',)

    # Define the layout of the admin form
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
        ('Translations', {
            'fields': ('question_translated', 'answer_translated')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')  # Make created_at and updated_at fields read-only