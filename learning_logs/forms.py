from django import forms
from .models import Topic
from .models import Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        # Создаем текстовое поле
        fields = ['text']
        labels = {'text':''}

# Форма создания новых записей
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        # Создаем текстовое поле в 80 колонок
        widgets = {'text': forms.Textarea(attrs={'cols':80})}