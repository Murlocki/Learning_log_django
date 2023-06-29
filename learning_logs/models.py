from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    # поле с заголовком темы
    text = models.CharField(max_length=200)

    # поле с датой
    date_added = models.DateTimeField(auto_now_add=True)

    #Владелец
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Создаем метод str для получения представления модели в виде строки
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Задаем множественную форму слова Entry
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text)>50:
            return self.text[:50]+'...'
        return self.text